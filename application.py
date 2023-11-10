import asyncio
from asyncio.tasks import Task
from engine.executor_engine_interface import ExecutorEngineInterface
from communication.communication_protocol import CommunicationProtocol, CommClientProtocol
from typing import Coroutine, Any, Dict, Union

class ScriptExecutor:
    def __init__(self, engine: ExecutorEngineInterface, comm: CommunicationProtocol):
        self.engine = engine
        self.comm = comm
        self.tasks: Dict[CommClientProtocol, Task[Union[str, Coroutine[Any, Any, str], None]]] = {}

    async def run_test(self) -> Coroutine[Any, Any, str]:
        return await self.engine.run_script()

    async def stop_test(self):
        return await self.engine.stop_script()

    async def current_status(self) -> str:
        print("Processing 'status' command...")

        await asyncio.sleep(3)
        print("'status' command has been processed")
        return "currentStatus"
    
    async def load_profile(self):
        pass

    async def load_product_info(self):
        pass
    
    async def message_callback(self, client: CommClientProtocol, message: str):
        task = None # Assign a default value to task
        if message == "status":
            task = asyncio.create_task(self.current_status())
        elif message == "run":
            task = asyncio.create_task(self.run_test())
        elif message == "stop":
            task = asyncio.create_task(self.stop_test())
        
        if task is not None:
            task.add_done_callback(lambda t: asyncio.create_task(
                self.comm.send_message(client, str(t.result()))))
            self.tasks[client] = task

    async def run(self):
        print("Starting application...")
        await self.comm.start()


if __name__ == "__main__":
    from engine.tag_script_engine import TAGScriptEngine
    from communication.tag_websocket_protocol import TAGWebsocketCommProtocol
    # You'll need to create instances of classes that implement the interfaces
    engine = TAGScriptEngine()
    comm = TAGWebsocketCommProtocol("localhost", 8765)
    executor = ScriptExecutor(engine, comm)
    comm.set_message_callback(executor.message_callback)
    asyncio.run(executor.run())