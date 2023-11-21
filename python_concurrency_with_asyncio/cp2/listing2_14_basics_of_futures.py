from asyncio import Future
from typing import Awaitable

my_future: Awaitable[int] = Future()

print(f'Is my_future done? {my_future.done()}')

my_future.set_result(42)

print(f'Is my_future done? {my_future.done()}')
print(f'What is the reulst of my_future? {my_future.result()}')