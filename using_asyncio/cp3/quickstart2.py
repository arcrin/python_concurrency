import asyncio
import time

async def main():
    try:
        print(f'{time.ctime()} Hello!')
        await asyncio.sleep(4.0)
        print(f'{time.ctime()} Goodbye!')
        return 'main'
    except asyncio.CancelledError:
        print(f'{time.ctime()} main() is cancelled!')

async def task1():
    try:
        print(f'{time.ctime()} Enter task1')
        await asyncio.sleep(3.0)
        print(f'{time.ctime()} Exit task1')
        return 1
    except asyncio.CancelledError:
        print(f'{time.ctime()} task1() is cancelled!')

async def task2():
    try:
        print(f'{time.ctime()} Enter task2')
        await asyncio.sleep(2.0)
        print(f'{time.ctime()} Exit task2')
        return 2
    except asyncio.CancelledError:
        print(f'{time.ctime()} task2() is cancelled!')

async def task3():
    try:
        print(f'{time.ctime()} Enter task3')
        await asyncio.sleep(1.0)
        print(f'{time.ctime()} Exit task3')
        return 3
    except asyncio.CancelledError:
        print(f'{time.ctime()} task3() is cancelled!')

loop = asyncio.get_event_loop()
task_main = loop.create_task(main())
task_1 = loop.create_task(task1())
task_2 = loop.create_task(task2())
task_3 = loop.create_task(task3())

loop.run_until_complete(task_3)
pending = asyncio.all_tasks(loop=loop)
for task in pending:
    task.cancel()
group = asyncio.gather(*pending, return_exceptions=True)
loop.run_until_complete(group)
loop.close()