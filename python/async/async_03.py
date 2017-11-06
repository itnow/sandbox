import asyncio
import functools


def event_handler(loop, stop=False):
    print('Event handler called')
    if stop:
        print('stopping the loop')
        loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        # In most case asyncio not supports args???, so we use partial:
        # The partial() is used for partial function application which
        # “freezes” some portion of a function’s arguments and/or keywords
        # resulting in a new object with a simplified signature.
        loop.call_later(2, functools.partial(event_handler, loop))
        print('starting event loop')
        loop.call_later(2, functools.partial(event_handler, loop, stop=True))
        loop.run_forever()
    finally:
        print('closing event loop')
        loop.close()
