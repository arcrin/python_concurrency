import trio

async def task1():
    await trio.sleep(2)
    print('task1 ended')

async def task2():
    await trio.sleep(1)
    print('task2 ended')    

async def main():
    async with trio.open_nursery() as nursery:
        nursery.start_soon(task1)
        nursery.start_soon(task2)

trio.run(main)