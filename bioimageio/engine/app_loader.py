from pydantic import BaseModel
from pathlib import Path
import logging
from yaml import safe_load
from typing import Optional
import importlib.util
from enum import Enum
from hypha_rpc.utils import ObjectProxy

logger = logging.getLogger(__name__)

class AppRuntime(Enum):
    python = "python"
    pyodide = "pyodide"
    triton = "triton"
    ray = "ray"

class AppInfo(BaseModel):
    name: str
    id: str
    description: str
    runtime: AppRuntime
    entrypoint: Optional[str] = None
        
    async def run(self, server):
        assert self.entrypoint
                    
        file_path = Path(__file__).parent / "apps" / self.id / self.entrypoint
        module_name = 'bioimageio.engine.apps.' + self.id.replace('-', '_')
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        if self.runtime == AppRuntime.python:
            spec.loader.exec_module(module)
            assert hasattr(module, "hypha_startup")
            await module.hypha_startup(server)
        else:
            raise NotImplementedError(f"Runtime {self.runtime} is not implemented yet.")

    
def load_apps():
    current_dir = Path(__file__).parent
    apps_dir = current_dir.parent.parent / "bioimageio/apps"
    # list folders under apps_dir
    apps = {}
    for app_dir in apps_dir.iterdir():
        if app_dir.is_dir():
            manifest_file = app_dir / "manifest.yaml"
            if manifest_file.exists():
                manifest = safe_load(manifest_file.read_text())
                app = AppInfo.model_validate(manifest)
                apps[app.id](app)
    return apps
