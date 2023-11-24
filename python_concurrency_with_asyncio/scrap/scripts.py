import asyncio
from util import async_timed

@async_timed()
async def task1():
    await asyncio.sleep(1)
@async_timed()
async def task2():
    await asyncio.sleep(1)
@async_timed()
async def task3():
    await asyncio.sleep(1)
@async_timed()
async def task4():
    await asyncio.sleep(1)
@async_timed()
async def task5():
    await asyncio.sleep(1)

async def end_task():
    await asyncio.sleep(1)  
    return 0
  