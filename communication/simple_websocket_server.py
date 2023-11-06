import asyncio
import websockets
from concurrent.futures import ThreadPoolExecutor

async def hello(websocket):
    while True:
        name = await websocket.recv()
        print(f"<<< {name}")

        greeting = f"Hello {name}!"

        await websocket.send(greeting)
        print(f">>> {greeting}")

async def user_input_task():
    with ThreadPoolExecutor() as executor:
        while True:
            loop = asyncio.get_event_loop()
            usr_input = await loop.run_in_executor(executor, input, "Enter something:")
            print(f"recv {usr_input}")

async def main():
    task = asyncio.create_task(user_input_task())
    async with websockets.serve(hello, "localhost", 8765):
        await asyncio.Future()  # run forever
    

if __name__ == "__main__":
    asyncio.run(main())