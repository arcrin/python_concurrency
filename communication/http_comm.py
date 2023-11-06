from aiohttp import web, ClientSession
from .communication_component_interface import CommunicationComponentInterface


class HttpCommComponent(CommunicationComponentInterface):
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.app = web.Application()
        self.app.router.add_post('/message', self.handler)
        self.clients = {}
        self.message_callback = None

    def set_message_callback(self, callback):
        self.message_callback = callback

    async def handler(self, request):
        data = await request.json()
        client_id = data.get('client_id')
        client_url = data.get('client_url')
        message = data.get('message')

        # Store the client's information
        self.clients[client_id] = client_url

        await self.message_callback(client_id, message)

    async def send_message(self, recipient, message):
        # Get the recipient's URL
        recipient_url = self.clients.get(recipient)
        if recipient_url is None:
            print(f"No client with id {recipient}")
            return
        
        async with ClientSession() as session:
            async with session.post(recipient_url, json={'message': message}) as response:
                print(f"Message sent to {recipient}, status: {response.status}")

    async def receive_message(self):
        # This function is not applicable in this context
        pass

    async def start(self):
        if self.message_callback is None:
            raise Exception("Message callback not set")
        runner = web.AppRunner(self.app)
        await runner.setup()
        site = web.TCPSite(runner, self.host, self.port)
        await site.start()