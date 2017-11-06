"""Standard Producer/Consumer Threading Pattern"""

import time
import threading
import queue as Queue


class Consumer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self._queue = queue

    def run(self):
        while True:
            # queue.get() blocks the current thread until
            # an item is retrieved.
            msg = self._queue.get()
            # Checks if the current message is the "Poison Pill"
            if isinstance(msg, str) and msg == 'quit':
                # if so, exists the loop
                break
            # "Processes" (or in our case, prints) the queue item
            print("I'm a thread, and I recieved: %s!" % msg)
        # Always be friendly :)
        print("Bye bye")


def producer():
    # Queue is used to share items between the threads.
    queue = Queue.Queue()

    # Create an instance of the worker
    worker = Consumer(queue)
    # start calls the internal run() method to kick off the thread
    worker.start()

    # variable to keep track of when we started
    start_time = time.time()
    # While under 5 seconds
    while time.time() - start_time < 5:
        # "Produce" a piece of work and stick it in
        # the queue for the Consumer to process
        queue.put('something at %s' % time.time())
        # Sleep a bit just to avoid an absurd number of messages
        time.sleep(1)

    # This the "poison pill" method of killing a thread.
    queue.put('quit')
    # wait for the thread to close down
    worker.join()


if __name__ == '__main__':
    producer()
