import trio

async def task1():
    with trio.move_on_after(3):
        print('task1 started')
        await trio.sleep(1)
        print('task1 ended')

if __name__ == '__main__':
    trio.run(task1)