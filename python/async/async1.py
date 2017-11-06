import random
import time
import asyncio


async def emmiter():
    random.seed()
    delay = random.randint(5, 10)
    asyncio.sleep(delay)
    print("Slept", delay, 'sec')


async def payload():
    start = time.time()
    for _ in range(5):
        await emmiter()
    print("Elapsed", time.time() - start, 'sec')


# payload()

loop = asyncio.get_event_loop()
loop.run_until_complete(payload())
loop.close()
