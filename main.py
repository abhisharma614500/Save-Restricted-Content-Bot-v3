# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import asyncio
from shared_client import start_client
import importlib
import os
import sys

async def load_and_run_plugins():
    await start_client()
    plugin_dir = "plugins"
    plugins = [f[:-3] for f in os.listdir(plugin_dir) if f.endswith(".py") and f != "__init__.py"]

    for plugin in plugins:
        module = importlib.import_module(f"plugins.{plugin}")
        if hasattr(module, f"run_{plugin}_plugin"):
            print(f"Running {plugin} plugin...")
            # यहाँ क्रैश से बचने के लिए टास्क के रूप में बैकग्राउंड में चलाया जा रहा है
            asyncio.create_task(getattr(module, f"run_{plugin}_plugin")())  

async def main():
    print("Starting clients ...")
    await load_and_run_plugins()
    # बॉट को हमेशा चालू रखने के लिए अनंत लूप
    while True:
        await asyncio.sleep(3600)  

if __name__ == "__main__":
    try:
        # आधुनिक और सुरक्षित तरीका जो लूप को अचानक बंद नहीं होने देता
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Shutting down...")
    except Exception as e:
        print(f"Error occurred: {e}")
        sys.exit(1)
