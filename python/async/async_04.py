import asyncio
import time


async def my_task(seconds):
    print('This task is taking {}s to complete'.format(seconds))
    time.sleep(seconds)
    return 'task finished'


if __name__ == '__main__':
    my_event_loop = asyncio.get_event_loop()
    try:
        print('task creation started')
        task_obj = my_event_loop.create_task(my_task(seconds=2))
        my_event_loop.run_until_complete(task_obj)
    finally:
        my_event_loop.close()

    print("Task's result was: {}".format(task_obj.result()))
