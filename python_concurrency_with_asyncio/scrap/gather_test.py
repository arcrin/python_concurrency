import asyncio
from scripts import *
from util import async_timed

class TaskManager:
    def __init__(self):
        self.task_queue = asyncio.Queue()
        self.task_list = [task1, task2, task3, task4, task5]
        self.running_tasks = []
        self.enqueue_task = None
        self.dequeue_task = None

    @async_timed()
    async def enqueue(self):
        for task in self.task_list:
            await self.task_queue.put(task)
            await asyncio.sleep(1)
        self.task_list.clear()
        if self.task_queue.empty():
            self.enqueue_task.cancel()
        await self.dequeue_task

    @async_timed()
    async def dequeue(self):
        while not (self.task_queue.empty() and self.task_list == []):
            try:
                task = await self.task_queue.get()
                self.running_tasks.append(asyncio.create_task(task()))
                await asyncio.sleep(0.1)
                print(len(self.task_list))

            except asyncio.CancelledError:
                print('dequeue cancelled')
                break
            except Exception as e:
                print(e)
                raise

    async def main(self):
        self.enqueue_task = asyncio.create_task(self.enqueue())
        self.dequeue_task = asyncio.create_task(self.dequeue())
        await asyncio.gather(self.enqueue_task, self.dequeue_task)

asyncio.run(TaskManager().main())