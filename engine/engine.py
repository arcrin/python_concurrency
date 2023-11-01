import asyncio

class ScriptExecutor:
    def __init__(self):
        self.script_task = None

    async def start_script(self, script):
        if self.script_task:
            self.script_task.cancel()
        self.script_task = asyncio.create_task(self.run_script(script))

    async def stop_script(self):
        if self.script_task:
            self.script_task.cancel()
            self.script_task = None

    async def run_script(self, script):
        while True:
            await script()
            await asyncio.sleep(1)  # Pause between script executions

# Usage
executor = ScriptExecutor()

async def test_script():
    print("Script is running")

await executor.start_script(test_script)
await asyncio.sleep(5)
await executor.stop_script()