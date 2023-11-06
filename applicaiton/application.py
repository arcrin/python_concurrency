import asyncio
from engine.executor_engine_interface import ExecutorEngineInterface
from communication.communication_component_interface import CommunicationComponentInterface

class ScriptExecutor:
    def __init__(self, engine: ExecutorEngineInterface, comm: CommunicationComponentInterface):
        self.engine = engine
        self.comm = comm
        self.tasks = {}

    async def run_test(self):
        return await self.engine.run_script()

    async def stop_test(self):
        return await self.engine.stop_script()

    async def current_status(self):
        await asyncio.sleep(3)
        return "currentStatus"
    
    async def message_callback(self, websocket, message):
        if message == "status":
            asyncio.create_task(self.comm.send_message(websocket, await self.current_status()))
        else:
            if message == "run":
                task = asyncio.create_task(self.run_test())
            elif message == "stop":
                task = asyncio.create_task(self.stop_test())
            
            task.add_done_callback(lambda t: asyncio.create_task(
                self.comm.send_message(websocket, t.result())))
            self.tasks[websocket] = task

    async def run(self):
        print("Starting application...")
        await self.comm.start()


if __name__ == "__main__":
    from engine.tag_script_engine import TAGScriptEngine
    from communication.websocket_com import WebSocketCommComponent
    # You'll need to create instances of classes that implement the interfaces
    engine = TAGScriptEngine()
    comm = WebSocketCommComponent("localhost", 8765)
    executor = ScriptExecutor(engine, comm)
    comm.set_message_callback(executor.message_callback)
    asyncio.run(executor.run())