import threading
import time


class ThreadingExample(object):
    """
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, interval=1):
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        # Run the thread in daemon mode. This allows the main application
        # to exit even though the thread is running. It will also (therefore)
        # make it possible to use ctrl+c to terminate the application.
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            print('Do something in the back')
            time.sleep(self.interval)


example = ThreadingExample()
time.sleep(3)
print('checkpoint')
time.sleep(5)
print('Bye')
