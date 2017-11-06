import threading
import time
import random


def worker(number):
    sleep = random.randrange(1, 10)
    time.sleep(sleep)
    print("{} worker, sleeping {} sec".format(number, sleep))


for i in range(10):
    t = threading.Thread(target=worker, args=(i,))
    t.start()


print('All workers was launched')
