import time
from concurrent.futures import ProcessPoolExecutor

def count(count_to: int) -> int:
    start = time.time()
    counter = 0
    while counter < count_to:
        counter += 1
    end = time.time()
    print(f'Finished couting to {count_to} in {end - start} seconds')
    return counter

if __name__ == '__main__':
    with ProcessPoolExecutor() as executor:
        numbers = [1, 3, 5, 22, 100000000]
        for result in executor.map(count, numbers):
            print(f'Counted to {result}')