import asyncio

# Create a task queue
task_queue = asyncio.Queue()

# Define a worker function to run tasks
async def worker():
    while True:
        task = await task_queue.get()  # Get the next task from the queue
        asyncio.create_task(task())  # Schedule the task to run
        task_queue.task_done()

# Define some example tasks
async def task1():
    await asyncio.sleep(1)
    print("\nTask 1 finished")

async def task2():
    await asyncio.sleep(2)
    print("\nTask 2 is finished")

# Function to get user input
def get_input():
    return input("Enter '1' or '2' to add tasks (or 'q' to quit): ")

async def main():
    # Create a worker task
    worker_task = asyncio.create_task(worker())

    while True:
        # Get user input in a separate thread
        user_input = await asyncio.get_event_loop().run_in_executor(None, get_input)

        if user_input == '1':
            await task_queue.put(task1)
            print("Task 1 added to the queue")
        elif user_input == '2':
            await task_queue.put(task2)
            print("Task 2 added to the queue")
        elif user_input == 'q':
            break
        else:
            print("Invalid input. Enter '1' or '2' to add tasks (or 'q' to quit)")

    # Add a None task to signal the worker to exit
    await task_queue.put(None)

    # Wait for the worker task to finish
    await worker_task

asyncio.run(main())