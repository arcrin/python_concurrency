import asyncio

class AsyncRange:
    def __init__(self, start, end):
        self.start = start 
        self.end = end

    def __aiter__(self):
        return self
    
    async def __anext__(self):
        if self.start >= self.end:
            value = self.start
            self.start += 1 
            return value
        else:
            raise StopAsyncIteration
        
async def main():
    async for number in AsyncRange(0, 3):
        print(number)


if __name__ == "__main__":
    asyncio.run(main())