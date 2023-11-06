import asyncio
import websockets
from .communication_component_interface import CommunicationComponentInterface

class WebSocketCommComponent(CommunicationComponentInterface):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connected = set()
        self.message_callback = None

    def set_message_callback(self, callback):
        self.message_callback = callback

    async def start(self):
        if self.message_callback is None:
            raise Exception("Message callback not set")
        await self.server()

    async def server(self):
        async with websockets.serve(self.handler, self.host, self.port):
            await asyncio.Future()  # run forever

    async def handler(self, client, path):
        # Register.
        self.connected.add(client)
        try:
            async for message in client:
                response = await self.message_callback(client, message)
        finally:
            # Unregister.
            self.connected.remove(client)

    async def send_message(self, client, message):
        await client.send(message)
        return "Message sent"

    async def receive_message(self):
        # This function is not applicable in this context
        pass