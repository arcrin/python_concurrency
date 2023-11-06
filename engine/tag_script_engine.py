from .executor_engine_interface import ExecutorEngineInterface
import asyncio

class TAGScriptEngine(ExecutorEngineInterface):
    async def run_script(self):
        print("Processing 'run' command...")
        await asyncio.sleep(5)
        print("'run' command has been processed")
        return "Script has been run"

    async def stop_script(self):
        await asyncio.sleep(5)
        print("Script has been stopped")
        return "Script has been stopped"