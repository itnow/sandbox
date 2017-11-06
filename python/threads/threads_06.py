# DOCS https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future

from time import sleep
from concurrent.futures import ThreadPoolExecutor


def do_some_task(message):
    sleep(5)
    return message


executor = ThreadPoolExecutor(3)
future = executor.submit(do_some_task, "hello")

print('is running?', future.running())
print('is done?', future.done())
sleep(5)
print('is done?', future.done())
print('result:', future.result())
