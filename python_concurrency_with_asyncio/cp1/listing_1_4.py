import multiprocessing
import os


def hello_from_process():
    print(f'Hello from a process! {multiprocessing.current_process()}')

if __name__ == '__main__':
    hello_process = multiprocessing.Process(target=hello_from_process)
    hello_process.start()

    print(f'Hello from parent process {os.getpid()}')
    hello_process.join()