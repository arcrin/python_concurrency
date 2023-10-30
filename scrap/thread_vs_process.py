import concurrent.futures
import time

def calculate_squares(start, end):
    squares = []
    for i in range(start, end):
        squares.append(i * i)
    return squares

if __name__ == '__main__':
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = []
        chunk_size = 250000
        for i in range(1, 1000001, chunk_size):
            future = executor.submit(calculate_squares, i, i + chunk_size)
            futures.append(future)
        results = []
        for future in concurrent.futures.as_completed(futures):
            results.extend(future.result())
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")

    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        futures = []
        chunk_size = 250000
        for i in range(1, 1000001, chunk_size):
            future = executor.submit(calculate_squares, i, i + chunk_size)
            futures.append(future)
        results = []
        for future in concurrent.futures.as_completed(futures):
            results.extend(future.result())
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")

