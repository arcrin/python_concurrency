import asyncio

# Create a task queue
task_queue = asyncio.Queue()

# Define a worker function to run tasks
async def worker():
    while True:
        task = await task_queue.get()  # Get the next task from the queue
        asyncio.create_task(task())  # Schedule the task to run
        task_queue.task_done()  # Mark the task as done

# Define some example tasks
async def task1():
    await asyncio.sleep(3)
    print("Task 1 is running")

async def task2():
    await asyncio.sleep(1)
    print("Task 2 is running")

# Add tasks to the task queue
async def add_tasks_to_queue():
    await task_queue.put(task1)
    await asyncio.sleep(1)  # Sleep for 1 second
    await task_queue.put(task2)

# Create a worker task to continuously process tasks
async def main():
    worker_task = asyncio.create_task(worker())

    # Add tasks to the queue
    await add_tasks_to_queue()

    # Wait for the worker to finish (for this example, we stop after a short time)
    await asyncio.sleep(3)
    worker_task.cancel()

asyncio.run(main())