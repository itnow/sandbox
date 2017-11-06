import asyncio
import aiohttp
import async_timeout


async def fetch(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()


async def main(loop):
    async with aiohttp.ClientSession(loop=loop) as session:
        html = await fetch(session, 'http://python.org')
        print(html[:300], '... [cuted]')


loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
