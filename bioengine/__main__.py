import sys
import argparse
import asyncio
import subprocess
import os

def start_server(args):
    # get current file path so we can get the path of apps under the same directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    command = [
        sys.executable,
        "-m",
        "hypha.server",
        f"--host={args.host}",
        f"--port={args.port}",
        f"--public-base-url={args.public_base_url}",
        "--startup-functions=bioengine:register_bioengine"
    ]
    subprocess.run(command)

def connect_server(args):
    from bioengine import connect_server
    if args.login_required:
        os.environ["BIOIMAGEIO_LOGIN_REQUIRED"] = "true"
    server_url = args.server_url
    loop = asyncio.get_event_loop()
    loop.create_task(connect_server(server_url))
    loop.run_forever()


def main():
    parser = argparse.ArgumentParser(description="BioImage.IO Chatbot utility commands.")
    
    subparsers = parser.add_subparsers()

    # Init command
    parser_init = subparsers.add_parser("init")
    parser_init.set_defaults(func=init)

    # Start server command
    parser_start_server = subparsers.add_parser("start-server")
    parser_start_server.add_argument("--host", type=str, default="0.0.0.0")
    parser_start_server.add_argument("--port", type=int, default=9000)
    parser_start_server.add_argument("--public-base-url", type=str, default="")
    parser_start_server.set_defaults(func=start_server)
    
    # Connect server command
    parser_connect_server = subparsers.add_parser("connect-server")
    parser_connect_server.add_argument("--server-url", default="https://ai.imjoy.io")
    parser_connect_server.add_argument("--login-required", action="store_true")
    parser_connect_server.set_defaults(func=connect_server)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()
        
if __name__ == '__main__':
    main()