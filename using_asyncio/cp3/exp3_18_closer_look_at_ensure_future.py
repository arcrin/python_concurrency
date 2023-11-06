import asyncio

async def f(): # it is a coroutine function, not a coroutine 
    pass

coro = f() # this is a coroutine
loop = asyncio.get_event_loop()

task = loop.create_task(coro)
assert isinstance(task, asyncio.Task)

new_task = asyncio.ensure_future(coro)
assert isinstance(new_task, asyncio.Task)

mystery_meat = asyncio.ensure_future(task)
assert mystery_meat is task