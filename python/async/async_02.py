import asyncio
import os
import urllib.request


URLS = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]


async def download_coroutine(url):
    req = urllib.request.urlopen(url)
    fname = os.path.basename(url)

    with open(fname, 'wb') as f:
        while True:
            chunk = req.read(1024)
            if not chunk:
                break
            f.write(chunk)

    msg = 'Downloaded {fname}'.format(fname=fname)
    return msg


async def main_routine(URLS):
    coroutines = [download_coroutine(url) for url in URLS]
    completed, pending = await asyncio.wait(coroutines)
    for item in completed:
        print(item.result())


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main_routine(URLS))
    finally:
        event_loop.close()
