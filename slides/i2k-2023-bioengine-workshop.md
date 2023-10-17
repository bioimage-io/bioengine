From Images to Knowledge Conference - 2023

## Web- and AI-powered Bioimage Analysis with the BioEngine

Wei OUYANG, Jeremy Metz

SciLifeLab | KTH Royal Institute of Technology, Stockholm
-----
## Overview
 * Introduction to the BioEngine
 * Hands on tutorial with the BioEngine

-----
## Challenges in AI for bioimaging

* **Usability**: User friendly GUI
* **Flexibility**: Flexible for different data types
* **Interactivity**: Respond to GUI on laptop/mobile
* **Scalability**: Remote storage and compute resources
* **Privacy**: Edge computing

-----
## Trends in Bioimaging
 * Use deep learning
 * Large models (transformers!)
 * Massive dataset
 * Scalabile file format (Zarr, N5, NGFF)

🚀A Future of Web- and AI-powered Bioimage Analysis

-----
## Existing solutions
* Desktop software: DeepImageJ, ilastik, napari
* Notebooks: Colab/ZeroCost4Mic, Jupyter Notebooks
* Web Apps: NucleAIzer, CellPose, DeepCell, ImJoy

-----
<!-- .slide: data-background="white" -->
### ImJoy https://imjoy.io
Data science tools in the browser

<img src="https://docs.google.com/drawings/d/e/2PACX-1vSBsdhDBrp4L2zWfL_9YOUHCS2zQ51HtjplGa-l_a1hMpNjbqENzmXrcSmYs6yed_NACNZSRH-7qsph/pub?w=1248&amp;h=573">

-----
# <img alt="BioImage Model Zoo" src="https://bioimage.io/static/img/bioimage-io-logo-white.svg">
### A repository for sharing AI Models in BioImage Analysis
-----
### https://bioimage.io

<img style="max-height: calc(100vh - 100px);" alt="BioImage Model Zoo screenshot" src="https://raw.githubusercontent.com/oeway/slides/master/2022/bioimage-model-zoo-screenshot.png">
-----
<!-- .slide: data-background="white" -->
## Meet the BioEngine
<img style="max-height: calc(100vh - 100px);" src="https://docs.google.com/drawings/d/e/2PACX-1vQCVUJDbgT_cPVsm--P75h13xbl7kW1Kt4RESW2opDb8MYOQrYQxToaFMFYdUwEBDBC4EWKwto0EExB/pub?w=1550&amp;h=983">

-----
<!-- .slide: data-background="white" -->
## Deploying the BioEngine
<img src="https://docs.google.com/drawings/d/e/2PACX-1vSoG7ywI0qbNAbG-bV7J9LomhlK8r1xyhxS70LcA4_XNt_oUiWoYLcMFJlUFB2oA80hgL5TQzAWUhNW/pub?w=1510&amp;h=1050">


-----
## BioEngine feature hightlights
* **Many models**
* **Many users**
* **Many applications**
* **Shared GPU resources**
* **Both inference and training**
* **Local or cloud deployment**

-----
# 🔥Hands on tutorial
Try the BioEngine

-----
<!-- .slide: data-state="tutorial-1" -->
## Tutorial 1: Getting Started
<button class="button" onclick='loadNotebook("1-bioengine-tutorial-i2k2022.ipynb", "tutorial-1-window", "https://raw.githubusercontent.com/bioimage-io/BioEngine/main/notebooks/1-bioengine-engine-tutorial.ipynb")'>Click to start the notebook</button>
<button id="tutorial-1-reset" class="button" style="background-color:red;display:none;" onclick='loadNotebook("1-bioengine-tutorial-i2k2022.ipynb", "tutorial-1-window", "https://raw.githubusercontent.com/bioimage-io/BioEngine/main/notebooks/1-bioengine-engine-tutorial.ipynb", true)'>Reset</button>
<div id="tutorial-1-window" style="width: 100%; height: 100vh;"></div>

-----
<!-- .slide: data-state="tutorial-3" -->
## Tutorial 2: Create UI with ImJoy and Kaibu
<button class="button" onclick='loadNotebook("3-bioengine-tutorial-i2k2022.ipynb", "tutorial-3-window", "https://raw.githubusercontent.com/bioimage-io/BioEngine/main/notebooks/3-kaibu-geojson.ipynb")'>Click to start the notebook</button>
<button id="tutorial-3-reset" class="button" style="background-color:red;display:none;" onclick='loadNotebook("3-bioengine-tutorial-i2k2022.ipynb", "tutorial-3-window", "https://raw.githubusercontent.com/bioimage-io/BioEngine/main/notebooks/3-kaibu-geojson.ipynb", true)'>Reset</button>
<div id="tutorial-3-window" style="width: 100%; height: 100vh;"></div>

-----
<!-- .slide: data-state="tutorial-2" -->
## Preview: Training a CellPose segmentation model
<button class="button" onclick='loadNotebook("2-bioengine-tutorial-i2k2022.ipynb", "tutorial-2-window", "https://raw.githubusercontent.com/bioimage-io/BioEngine/main/notebooks/2-bioengine-model-training.ipynb")'>Click to start the notebook</button>
<button id="tutorial-2-reset" class="button" style="background-color:red;display:none;" onclick='loadNotebook("2-bioengine-tutorial-i2k2022.ipynb", "tutorial-2-window", "https://raw.githubusercontent.com/bioimage-io/BioEngine/main/notebooks/2-bioengine-model-training.ipynb", true)'>Reset</button>
<div id="tutorial-2-window" style="width: 100%; height: 100vh;"></div>

-----
<!-- .slide: data-state="tutorial-4" -->
## Preview: Model training with the BioEngine
<button class="button" onclick='loadNotebook("4-bioengine-tutorial-i2k2022.ipynb", "tutorial-4-window", "https://raw.githubusercontent.com/bioimage-io/BioEngine/main/notebooks/4-kaibu-interactive-training.ipynb")'>Click to start the notebook</button>
<button id="tutorial-4-reset" class="button" style="background-color:red;display:none;" onclick='loadNotebook("4-bioengine-tutorial-i2k2022.ipynb", "tutorial-3-window", "https://raw.githubusercontent.com/bioimage-io/BioEngine/main/notebooks/4-kaibu-interactive-training.ipynb", true)'>Reset</button>
<div id="tutorial-4-window" style="width: 100%; height: 100vh;"></div>

-----
## BioEngine vs Jupyter Notebooks / Colab
 Scalability!
 * Cloud & On-premise deployment
 * For multi-user or the public
 * Multi-model serving
 * Improved GPU utilization
 * Instant usage without setup or installation

-----
## Accessing the BioEngine from Icy
<img src="https://raw.githubusercontent.com/oeway/slides/master/2022/icy-bioengine-cellpose-demo.gif">

Collabration with Carlos García López de Haro and the Icy Team

-----
## Accessing the BioEngine from Icy
<img src="https://raw.githubusercontent.com/oeway/slides/master/2022/icy-bioengine-demo-nuclei-segmentation.gif">

Collabration with Carlos García López de Haro and the Icy Team

-----
## 🚀AI-assisted Bioimage Analysis
<iframe width="560" height="315" src="https://www.youtube.com/embed/pkOp_oUybsc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Powered by OpenAI GPT-3 and Codex
-----
## Conclusions
 * BioEninge for scalable AI model serving
 * How to use the BioEngine

-----
### Acknowledgements (1)
Work carried out at Cell Profiling group @ SciLifeLab headed by Emma Lundberg

ImJoy is powered by the 🧠 and ❤️ of the ImJoy Team including:
 * Florian Mueller
 * Martin Hjelmare
 * Craig Russell
 * ...

Follow us on twitter @ImJoyTeam

-----
### Acknowledgements (2)

BioImage.IO is powered by the 🧠 and ❤️ of:
 * deepImageJ Team
 * EBI Bioimage Archive Team
 * Fiji/ImageJ Team
 * ilastik Team
 * ImJoy Team
 * ZeroCostDL4Mic Team
 * ...

Follow us on twitter @bioimageio

-----

# 🙏Thank You!



<!-- startup script  -->
```javascript execute

async function loadNotebook(name, window_id, url, overwrite){
    const jupyter = await api.createWindow({src: "https://jupyter.imjoy.io/lab/index.html", window_id})
    const bid = window_id.replace("window", "reset")
    const button = document.getElementById(bid)
    if(await jupyter.fileExists(name)){
        if(overwrite){
            const content = await (await fetch(url)).text()
            await jupyter.removeFile(name)
            await jupyter.loadFile(name, content, 'application/json')
        }
        await jupyter.openFile(name)
    } else{
        const content = await (await fetch(url)).text()
        const filePath = await jupyter.loadFile(name, content, 'application/json')
        await jupyter.openFile(filePath)
    }
    button.style.display = "inline-block";
}


const PythonPluginCode = `
<config lang="json">
{
  "name": "PythonPlugin",
  "type": "native-python",
  "version": "0.1.0",
  "description": "[TODO: describe this plugin with one sentence.]",
  "tags": [],
  "ui": "",
  "cover": "",
  "inputs": null,
  "outputs": null,
  "flags": [],
  "icon": "extension",
  "api_version": "0.1.8",
  "env": "",
  "permissions": [],
  "requirements": [],
  "dependencies": []
}
</config>

<script lang="python">
from imjoy import api


class ImJoyPlugin():
    def setup(self):
        api.showMessage('Python plugin initialized')

    def add(self, a, b):
        return a + b

api.export(ImJoyPlugin())
</script>
`

const JSPluginCode = `
<config lang="json">
{
  "name": "JSPlugin",
  "type": "window",
  "tags": [],
  "ui": "",
  "version": "0.1.0",
  "cover": "",
  "description": "[TODO: describe this plugin with one sentence.]",
  "icon": "extension",
  "inputs": null,
  "outputs": null,
  "api_version": "0.1.8",
  "env": "",
  "permissions": [],
  "requirements": [],
  "dependencies": [],
  "defaults": {"w": 20, "h": 10}
}
</config>

<script lang="javascript">
window.callPython = async function(){
    const pythonPlugin = await api.getPlugin('PythonPlugin')
    const result = await pythonPlugin.add(10, 99)
    document.getElementById("result").innerHTML = "10 + 99 =" + result
}

class ImJoyPlugin {
  async setup() {
    api.log('initialized')
  }

  async run(ctx) {
  }
}
api.export(new ImJoyPlugin())
</script>

<window lang="html">
  <div>
    <button class="button" onclick="callPython()"> Calculate in Python</button>
    <h3 id="result"></h3>
  </div>
</window>
`

window.ZarrPythonCode = `
<config lang="json">
{
  "name": "ZarrPythonPlugin",
  "type": "native-python",
  "version": "0.1.0",
  "description": "[TODO: describe this plugin with one sentence.]",
  "tags": [],
  "ui": "",
  "cover": "",
  "inputs": null,
  "outputs": null,
  "flags": [],
  "icon": "extension",
  "api_version": "0.1.8",
  "env": "",
  "permissions": [],
  "requirements": ["zarr", "fsspec"],
  "dependencies": []
}
</config>

<script lang="python">
import zarr
from imjoy_rpc import api
from imjoy_rpc import register_default_codecs
from fsspec.implementations.http import HTTPFileSystem
register_default_codecs()

fs = HTTPFileSystem()
http_map = fs.get_mapper("https://openimaging.github.io/demos/multi-scale-chunked-compressed/build/data/medium.zarr")
z_group = zarr.open(http_map, mode='r')

class ImJoyPlugin:
    async def setup(self):
        pass

    async def run(self, ctx):
        viewer = await api.createWindow(
            src="https://kitware.github.io/itk-vtk-viewer/app/",
            name="ITK/VTK Viewer"
        )
        await viewer.setImage(z_group)

api.export(ImJoyPlugin())
</script>
`
function startImageJ(){
  api.createWindow({src:"https://ij.imjoy.io", name:"ImageJ.JS"})  
}

async function initializeMacroEditor(editor_container, code){
    const editorElm = document.getElementById(editor_container);
    if(!editorElm) throw new Error("editor container not found: " + editor_container)
    editorElm.style.width = '90%';
    editorElm.style.display = 'inline-block';
    editorElm.style.height = 'calc(100vh - 200px)';
    // force update the slide
    Reveal.layout();
    let editorWindow;
    const config = {lang: 'javascript'}
    config.templates = [
        {
          name: "New",
          url: null,
          lang: 'javascript',
        },
        {
          name: "Sphere",
          url: "https://wsr.imagej.net/download/Examples/Macro/Sphere.ijm",
          lang: 'javascript',
        },
        {
          name: "OpenDialog Demo",
          url: "https://wsr.imagej.net/download/Examples/Macro/OpenDialog_Demo.ijm",
          lang: 'javascript',
        },
        {
          name: "Overlay",
          url: "https://wsr.imagej.net/download/Examples/Macro/Overlay.ijm",
          lang: 'javascript',
        }
      ]
    config.ui_elements = {
      run: {
          _rintf: true,
          type: 'button',
          label: "Run",
          icon: "play",
          visible: true,
          shortcut: 'Shift-Enter',
          async callback(content) {
              try {
                  let ij = await api.getWindow("ImageJ.JS-" + editor_container)
                  if(!ij){
                      //put the editor side by side
                      editorElm.style.width = '38.2%';
                      const ijElm = document.createElement('div');
                      ijElm.id = 'imagej-' + editor_container
                      ijElm.style.display = 'inline-block';
                      ijElm.style.width = '61.8%';
                      ijElm.style.height = editorElm.style.height;
                      editorElm.parentNode.insertBefore(ijElm, editorElm.nextSibling);
                      ij = await api.createWindow({src:"https://ij.imjoy.io", name:"ImageJ.JS-" + editor_container, window_id: 'imagej-' + editor_container})
                  }
                  await ij.runMacro(content)
              } catch (e) {
                  api.showMessage("Failed to run macro, error: " + e.toString());
              } finally {
                  editorWindow.updateUIElement('stop', {
                      visible: false
                  })
                  editorWindow.setLoader(false);
                  api.showProgress(100);
              }
          }
      },
    }
    editorWindow = await api.createWindow({
        src: 'https://if.imjoy.io',
        name: 'ImageJ Script Editor',
        config,
        window_id: editor_container,
        data: {code}
    })
}

Reveal.addEventListener('ij-macro-1', async ()=>{
    const code = `run("Blobs (25K)");
setAutoThreshold("Default");
setOption("BlackBackground", true);
run("Convert to Mask");
run("Analyze Particles...", "size=5-Infinity add");
`
    initializeMacroEditor('macro-editor-1', code)
})

Reveal.addEventListener('demo1', async function(){
    await api.createWindow({src: 'https://if.imjoy.io', config: {fold: [1]}, data: {code: PythonPluginCode}, window_id: "window-1"})

    await api.createWindow({src: 'https://if.imjoy.io', config: {fold: [1, 29]}, data: {code: JSPluginCode}, window_id: "window-2"})
})

async function runDemo2(){
 const viewer = await api.showDialog({src: "https://kaibu.org/#/app", name: "Kaibu"})
        await viewer.view_image("https://images.proteinatlas.org/61448/1319_C10_2_blue_red_green.jpg")
        await viewer.add_shapes([], {name:"annotation"})
}

async function runHPADemo(){
    const plugin = await api.getPlugin("https://gist.githubusercontent.com/oeway/b318a26ef7191679b175be5216accbda/raw/HPA-UMAP-Studio.imjoy.html")
    await plugin.run({})
}


function startImageJ(){
  api.createWindow({src:"https://ij.imjoy.io", name:"ImageJ.JS"})  
}

async function initializeMacroEditor(editor_container, code){
    const editorElm = document.getElementById(editor_container);
    if(!editorElm) throw new Error("editor container not found: " + editor_container)
    editorElm.style.width = '90%';
    editorElm.style.display = 'inline-block';
    editorElm.style.height = 'calc(100vh - 200px)';
    // force update the slide
    Reveal.layout();
    let editorWindow;
    const config = {lang: 'javascript'}
    config.templates = [
        {
          name: "New",
          url: null,
          lang: 'javascript',
        },
        {
          name: "Sphere",
          url: "https://wsr.imagej.net/download/Examples/Macro/Sphere.ijm",
          lang: 'javascript',
        },
        {
          name: "OpenDialog Demo",
          url: "https://wsr.imagej.net/download/Examples/Macro/OpenDialog_Demo.ijm",
          lang: 'javascript',
        },
        {
          name: "Overlay",
          url: "https://wsr.imagej.net/download/Examples/Macro/Overlay.ijm",
          lang: 'javascript',
        }
      ]
    config.ui_elements = {
      run: {
          _rintf: true,
          type: 'button',
          label: "Run",
          icon: "play",
          visible: true,
          shortcut: 'Shift-Enter',
          async callback(content) {
              try {
                  let ij = await api.getWindow("ImageJ.JS-" + editor_container)
                  if(!ij){
                      //put the editor side by side
                      editorElm.style.width = '38.2%';
                      const ijElm = document.createElement('div');
                      ijElm.id = 'imagej-' + editor_container
                      ijElm.style.display = 'inline-block';
                      ijElm.style.width = '61.8%';
                      ijElm.style.height = editorElm.style.height;
                      editorElm.parentNode.insertBefore(ijElm, editorElm.nextSibling);
                      ij = await api.createWindow({src:"https://ij.imjoy.io", name:"ImageJ.JS-" + editor_container, window_id: 'imagej-' + editor_container})
                  }
                  await ij.runMacro(content)
              } catch (e) {
                  api.showMessage("Failed to run macro, error: " + e.toString());
              } finally {
                  editorWindow.updateUIElement('stop', {
                      visible: false
                  })
                  editorWindow.setLoader(false);
                  api.showProgress(100);
              }
          }
      },
    }
    editorWindow = await api.createWindow({
        src: 'https://if.imjoy.io',
        name: 'ImageJ Script Editor',
        config,
        window_id: editor_container,
        data: {code}
    })
}

Reveal.addEventListener('ij-macro-1', async ()=>{
    const code = `run("Blobs (25K)");
setAutoThreshold("Default");
setOption("BlackBackground", true);
run("Convert to Mask");
run("Analyze Particles...", "size=5-Infinity add");
`
    initializeMacroEditor('macro-editor-1', code)
})

Reveal.addEventListener('ij-macro-2', async ()=>{
    const response = await fetch("https://wsr.imagej.net/download/Examples/Macro/Colors_of_2021.ijm")
    const code = await response.text()
    initializeMacroEditor('macro-editor-2', code)
})

```