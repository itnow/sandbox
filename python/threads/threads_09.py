# DOCS http://masnun.com/2016/03/29/python-a-quick-introduction-to-the-concurrent-futures-module.html

from time import sleep
from random import randint
from concurrent.futures import ThreadPoolExecutor, wait, as_completed


def do_some_task(num):
    sleep(randint(1, 5))
    return "Return of {}".format(num)


pool = ThreadPoolExecutor(3)
futures = []
for x in range(5):
    futures.append(pool.submit(do_some_task, x))

for x in as_completed(futures):
    print(x.result())

# The wait() function would return a named tuple which contains two set:
# one set contains the futures which completed (either got result or exception)
# and the other set containing the ones which didn’t complete.

# We can control the behavior of the wait function by defining when it should
# return. We can pass one of these values to the return_when param
# of the function: FIRST_COMPLETED, FIRST_EXCEPTION and ALL_COMPLETED.
# By default, it’s set to ALL_COMPLETED, so the wait function returns only
# when all futures complete. But using that parameter, we can choose
# to return when the first future completes or first exception encounters.
print(wait(futures))
