import threading

def hello_from_thread():
    print(f'Hello from a thread! {threading.current_thread()}')

hello_thread = threading.Thread(target=hello_from_thread)
hello_thread.start()

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f'Python i currently running {total_threads} threads')
print(f'The current thread is {thread_name}')

hello_thread.join()