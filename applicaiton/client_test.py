import aioconsole
import websockets
import asyncio

async def send_messages(websocket):
    while True:
        command = await aioconsole.ainput("Enter a command: ")
        await websocket.send(command)
        print(f"Sent: '{command}'")

async def receive_messages(websocket):
    while True:
        response = await websocket.recv()
        print(f"\nReceived: {response}")

async def test_client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        send_task = asyncio.create_task(send_messages(websocket))
        receive_task = asyncio.create_task(receive_messages(websocket))
        await asyncio.gather(send_task, receive_task)

asyncio.run(test_client())