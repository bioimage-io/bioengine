import micropip
await micropip.install(["ssl", "fastapi==0.70.0"])

import random
import string
import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

def create_fastapi_app(server_url):
    app = FastAPI()
    
    @app.get("/files/{path:path}")
    async def serve_my_app(path: str):
        # Construct the full file path
        file_path = os.path.abspath(os.path.join("/mnt", path))
        
        # Security check: Ensure the file path is within /mnt directory
        if not file_path.startswith(os.path.abspath("/mnt")):
            raise HTTPException(status_code=400, detail="Invalid file path")

        # Check if the path is a file and serve it
        if os.path.isfile(file_path):
            return FileResponse(file_path)
        else:
            raise HTTPException(status_code=404, detail="File not found")
        
    @app.get("/", response_class=HTMLResponse)
    async def index():
        files = os.listdir("/mnt")
        return f'''
        <html>
            <head>
                <title>Hello</title>
            </head>
            <body>
                <h1>Files</h1>
                <ul>
                    {"".join([f'<li><a href="./files/{f}">{f}</a></li>' for f in files])}
                </ul>
                <br>
                <img style="width: 500px" src="https://cataas.com/cat">
            </body>
        </html>
        '''
    return app

async def hypha_startup(server):
    # Registering fastapi app
    connection_info = await server.get_connection_info()
    fastapi_app = create_fastapi_app(connection_info["public_base_url"])
    async def serve_fastapi(args):
        scope = args["scope"]
        print(f'{scope["client"]} - {scope["method"]} - {scope["path"]}')
        await fastapi_app(args["scope"], args["receive"], args["send"])

    await server.register_service({
        "id": "http-" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)),
        "name": "FastAPI HTTP App",
        "description": "A http server to serve all the mounted files in a simple example page.",
        "type": "ASGI",
        "serve": serve_fastapi,
        "config":{
            "visibility": "public"
        },
        "example_script": f"""print("HTTP server running at {connection_info.public_base_url}/{server.config['workspace']}/apps/fastapi-http-app/")"""
    })
    
    print(f"Server app running at {connection_info.public_base_url}/{server.config['workspace']}/apps/fastapi-http-app/")

print("Hypha startup script loaded")