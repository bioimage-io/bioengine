import logging
import sys, os
import imagej
import scyjava as sj
import asyncio
import traceback
import numpy as np
import xarray as xr
from jpype import JOverride, JImplements
import argparse
from hypha_rpc import connect_to_server
    

logger = logging.getLogger(__name__)
os.environ["JAVA_HOME"] = os.sep.join(sys.executable.split(os.sep)[:-2] + ["jre"])

def capture_console(ij, print=True):
    logs = {}
    logs["stdout"] = []
    logs["stderr"] = []

    @JImplements("org.scijava.console.OutputListener")
    class JavaOutputListener:
        @JOverride
        def outputOccurred(self, e):
            source = e.getSource().toString
            output = e.getOutput()

            if print:
                if source == "STDOUT":
                    sys.stdout.write(output)
                    logs["stdout"].append(output)
                elif source == "STDERR":
                    sys.stderr.write(output)
                    logs["stderr"].append(output)
                else:
                    output = "[{}] {}".format(source, output)
                    sys.stderr.write(output)
                    logs["stderr"].append(output)

    ij.py._outputMapper = JavaOutputListener()
    ij.console().addOutputListener(ij.py._outputMapper)
    return logs


def format_logs(logs):
    output = ""
    if logs["stdout"]:
        output += "STDOUT:\n"
        output += "\n".join(logs["stdout"])
        output += "\n"
    if logs["stderr"]:
        output += "STDERR:\n"
        output += "\n".join(logs["stderr"])
        output += "\n"
    return output


def get_module_info(ij, custom_script, name=None):
    name = name or "scijava_script"
    ScriptInfo = sj.jimport("org.scijava.script.ScriptInfo")
    StringReader = sj.jimport("java.io.StringReader")
    moduleinfo = ScriptInfo(ij.getContext(), name, StringReader(custom_script))
    inputs = {}
    outputs = {}

    for inp in ij.py.from_java(moduleinfo.inputs()):
        input_type = str(inp.getType().getName())
        input_name = str(inp.getName())
        print(input_type, input_name)
        inputs[input_name] = {"name": input_name, "type": input_type}

    for outp in ij.py.from_java(moduleinfo.outputs()):
        output_type = str(outp.getType().getName())
        output_name = str(outp.getName())
        outputs[output_name] = {"name": output_name, "type": output_type}

    return {"id": moduleinfo.getIdentifier(), "outputs": outputs, "inputs": inputs}


def check_size(array):
    result_bytes = array.tobytes()
    if len(result_bytes) > 20000000:  # 20MB
        raise Exception(
            f"The data is too large ({len(result_bytes)} bytes) to be transfered."
        )


async def execute(config, context=None):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, run_imagej, config)


def run_imagej(config):
    mode = config.get("mode", "headless")
    logger.info("Initializing ImageJ...")
    ij = imagej.init(os.environ.get("IMAGEJ_DIR"), mode=mode)
    logger.info("Running ImageJ macro...")
    try:
        WindowManager = sj.jimport("ij.WindowManager")
        ImagePlus = sj.jimport("ij.ImagePlus")
        logs = capture_console(ij)
        script = config.get("script")
        lang = config.get("lang", "ijm")
        assert script is not None, "script is required"
        module_info = get_module_info(ij, script)
        inputs_info = module_info["inputs"]
        outputs_info = module_info["outputs"]
        inputs = config.get("inputs", {})
        select_outputs = config.get("select_outputs")
        args = {}
        for k in inputs:
            if isinstance(inputs[k], (np.ndarray, np.generic, dict)):
                if isinstance(inputs[k], (np.ndarray, np.generic)):
                    if inputs[k].ndim == 2:
                        dims = ["x", "y"]
                    elif inputs[k].ndim == 3 and inputs[k].shape[2] in [1, 3, 4]:
                        dims = ["x", "y", "c"]
                    elif inputs[k].ndim == 3 and inputs[k].shape[0] in [1, 3, 4]:
                        dims = ["c", "x", "y"]
                    elif inputs[k].ndim == 3:
                        dims = ["z", "x", "y"]
                    elif inputs[k].ndim == 4:
                        dims = ["z", "x", "y", "c"]
                    elif inputs[k].ndim == 5:
                        dims = ["t", "z", "x", "y", "c"]
                    else:
                        raise Exception(f"Unsupported ndim: {inputs[k].ndim}")
                    inputs[k] = {"data": inputs[k], "dims": dims}

                img = inputs[k]
                assert isinstance(
                    img, dict
                ), f"input {k} must be a dictionary or a numpy array"
                assert "data" in img, f"data is required for {k}"
                assert "dims" in img, f"dims is required for {k}"
                da = xr.DataArray(
                    data=img["data"],
                    dims=img["dims"],
                    attrs=img.get("attrs", {}),
                    name=k,
                )
                inputs[k] = ij.py.to_java(da)
                if lang == "ijm":
                    # convert to ImagePlus
                    inputs[k] = ij.convert().convert(inputs[k], ImagePlus)
                    if inputs[k]:
                        inputs[k].setTitle(k)
                        # Display the image
                        if mode != "headless":
                            inputs[k].show()
                else:
                    raise NotImplementedError(
                        "Don't know how to display the image (only ijm is supported)."
                    )
            if k in inputs_info:
                args[k] = ij.py.to_java(inputs[k])

        # Run the script
        macro_result = ij.py.run_script(lang, script, args)
        results = {}
        if select_outputs is None:
            select_outputs = list(outputs_info.keys())
        for k in select_outputs:
            if k in outputs_info:
                results[k] = macro_result.getOutput(k)
                if results[k] and not isinstance(results[k], (int, str, float, bool)):
                    try:
                        results[k] = ij.py.from_java(results[k]).to_numpy()
                        check_size(results[k])
                    except Exception:
                        # TODO: This is needed due to a bug in pyimagej for converting java string
                        if str(type(results[k])) == "<java class 'java.lang.String'>":
                            results[k] = str(results[k])
                        else:
                            results[k] = {
                                "type": str(type(results[k])),
                                "text": str(results[k]),
                            }
            else:
                # If the output name is not in the script annotation,
                # Try to get the image from the WindowManager by title
                img = WindowManager.getImage(k)
                if not img:
                    raise Exception(f"Output not found: {k}\n{format_logs(logs)}")
                results[k] = ij.py.from_java(img).to_numpy()
                check_size(results[k])
    except Exception as exp:
        raise exp
    finally:
        ij.dispose()

    return {"outputs": results, "logs": logs}


test_macro = """
#@ String name
#@ int age
#@ String city
#@output Object greeting
greeting = "Hi " + name + ". You are " + age + " years old, and live in " + city + "."
"""


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--server-url", type=str, help="Server URL")
    parser.add_argument("--workspace", type=str, help="Workspace")
    parser.add_argument("--token", type=str, help="Token")
    parser.add_argument("--service-id", type=str, help="ImageJ Service ID")
    
    args = parser.parse_args()
    logger.info("Connecting to the server %s, workspace: %s", args.server_url, args.workspace)
    # get server_url and token from url
    server = await connect_to_server({
        "server_url": args.server_url,
        "workspace": args.workspace,
        "token": args.token,
    })
    try:
        logger.info("Testing the imagej service...")
        ret = await execute(
            {
                "script": test_macro,
                "inputs": {"name": "Tom", "age": 20, "city": "Shanghai"},
            }
        )
        outputs = ret["outputs"]
        assert (
            outputs["greeting"] == "Hi Tom. You are 20 years old, and live in Shanghai."
        )
    except Exception:
        print(traceback.format_exc())
        sys.exit(1)

    logger.info("Starting the imagej service...")
    svc = await server.register_service(
        {
            "id": args.service_id,
            "type": "imagej",
            "config": {"require_context": True, "visibility": "public"},
            "execute": execute,
        }
    )
    logger.info(f"ImageJ service is registered as `{svc['id']}`")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
    
