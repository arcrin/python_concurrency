import asyncio

async def task1():
    for i in range(10):
        print(f'task1 iteration {i}')
        await asyncio.sleep(1)
    print('task1 done')

async def task2():
    for i in range(10):
        print(f'task2 iteration {i}')
        await asyncio.sleep(1.5)
    print('task2 done')


async def main():
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())
    await asyncio.gather(*[t1, t2])

asyncio.run(main())