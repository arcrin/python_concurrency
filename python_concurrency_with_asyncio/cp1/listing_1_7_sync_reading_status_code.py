import time
import requests

def read_google() -> None:
    response = requests.get('https://google.com')
    print(response.status_code)

sync_start = time.time()

read_google()
read_google()

sync_end = time.time()

print(f'Running synchronously, this took {sync_end - sync_start:.4f} seconds')