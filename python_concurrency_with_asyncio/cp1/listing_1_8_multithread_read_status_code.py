import time
import threading
import requests

def read_google() -> None:
    response = requests.get('https://google.com')
    print(response.status_code)

thread_1 = threading.Thread(target=read_google)
thread_2 = threading.Thread(target=read_google)

thread_start = time.time()

thread_1.start()
thread_2.start()

print('All threads running!')

thread_1.join()
thread_2.join()

thread_end = time.time()

print(f'Running with threads took {thread_end - thread_start:.4f} seconds')