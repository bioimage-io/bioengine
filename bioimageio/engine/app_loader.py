from pydantic import BaseModel
from pathlib import Path
import logging
from yaml import safe_load
from typing import Callable, Optional
import sys
import importlib.util

logger = logging.getLogger(__name__)

# define runtime type enum for app runtime
class AppRuntime(str):
    python = "python"
    pyodide = "pyodide"
    triton = "triton"

class AppInfo(BaseModel):
    name: str
    id: str
    description: str
    runtime: AppRuntime
    entrypoint: Optional[str] = None
    
    async def run(self, server):
        if self.runtime == AppRuntime.python:
            assert self.entrypoint
                        
            file_path = Path(__file__).parent.parent / "apps" / self.id / self.entrypoint
            module_name = 'bioimageio.engine.apps.' + self.id.replace('-', '_')
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            assert hasattr(module, "hypha_startup")
            await module.hypha_startup(server)

def load_apps():
    current_dir = Path(__file__).parent
    apps_dir = current_dir.parent / "apps"
    # list folders under apps_dir
    apps = []
    for app_dir in apps_dir.iterdir():
        if app_dir.is_dir():
            manifest_file = app_dir / "manifest.yaml"
            if manifest_file.exists():
                manifest = safe_load(manifest_file.read_text())
                apps.append(AppInfo.parse_obj(manifest))
    return apps