from typing import Any
import asyncio

def handle_result(fut: asyncio.Future[Any]):
    if fut.cancelled():
        print('Future was cancelled')
    elif fut.exception():
        print(f"Future raised an exception: {fut.exception()}")
    else:
        print(f"Future result: {fut.result()}")



