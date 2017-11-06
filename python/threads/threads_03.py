import time
import urllib.request as ur
from concurrent.futures import ThreadPoolExecutor


# from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

urls = [
    'http://www.python.org',
    'http://www.python.org/about/',
    'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
    'http://www.python.org/doc/',
    'http://www.python.org/download/',
    'http://www.python.org/getit/',
    'http://www.python.org/community/',
    'https://wiki.python.org/moin/',
    'http://planet.python.org/',
    'https://wiki.python.org/moin/LocalUserGroups',
    'http://www.python.org/psf/',
    'http://docs.python.org/devguide/',
    'http://www.python.org/community/awards/'
]


# V1
print('=== ThreadPoolExecutor')
start_time = time.time()
with ThreadPoolExecutor(max_workers=4) as executor:
    results = executor.map(ur.urlopen, urls)
for r in results:
    print('--- ', r.getcode(), r.geturl())
print("=== Time taken: {}".format(time.time() - start_time))

# V2
print('=== ThreadPool')
start_time = time.time()
pool = ThreadPool(4)
# Open the urls in their own threads
# and return the results
results = pool.map(ur.urlopen, urls)
# close the pool and wait for the work to finish
pool.close()
pool.join()
for r in results:
    print('--- ', r.getcode(), r.geturl())
print("=== Time taken: {}".format(time.time() - start_time))

# V3
print('=== Single thread')
start_time = time.time()
for url in urls:
    r = ur.urlopen(url)
    print('--- ', r.getcode(), r.geturl())
print("=== Time taken: {}".format(time.time() - start_time))
