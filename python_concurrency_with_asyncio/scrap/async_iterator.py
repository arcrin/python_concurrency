import asyncio

class AsyncCounter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current < self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopAsyncIteration

# Usage:
async def main():
    async for number in AsyncCounter(0, 5):
        print(number)

if __name__ == '__main__':
    asyncio.run(main())