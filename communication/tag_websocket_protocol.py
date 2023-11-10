import asyncio
import websockets
from websockets.server import WebSocketServerProtocol
from typing import Set, Callable, Coroutine, Any
from .communication_protocol import CommClientProtocol

class TAGWebsocketCommProtocol:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.connected: Set[WebSocketServerProtocol] = set()
        self.message_callback = None

    def set_message_callback(self, callback: Callable[[CommClientProtocol, str], Coroutine[Any, Any, None]]):
        self.message_callback = callback

    async def start(self):
        if self.message_callback is None:
            raise Exception("Message callback not set")
        await self.server()

    async def server(self):
        async with websockets.serve(self.handler, self.host, self.port):
            await asyncio.Future()

    async def handler(self, client: WebSocketServerProtocol, path: str):
        # Register.
        self.connected.add(client)
        try:
            async for message in client:
                if self.message_callback is not None:
                    await self.message_callback(client, str(message))
        finally:
            # Unregister.
            self.connected.remove(client)

    async def send_message(self, client: CommClientProtocol, message: str):
        await client.send(message)