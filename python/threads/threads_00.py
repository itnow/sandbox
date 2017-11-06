import threading
import time


def worker():
    print(threading.currentThread().getName(), "Start")
    time.sleep(3)
    print(threading.currentThread().getName(), "Stop")


w = threading.Thread(name='not_daemon', target=worker)


while True:
    time.sleep(4)
    w.run()
