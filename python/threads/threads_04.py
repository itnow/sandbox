import time
from concurrent.futures import ThreadPoolExecutor
# from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

payload = [(x, 123456) for x in range(320, 330)]


def powpow(xy):
    x, y = xy
    return x**y


# V1
print('=== ThreadPoolExecutor')
start_time = time.time()
with ThreadPoolExecutor(max_workers=4) as executor:
    results = executor.map(powpow, payload)
for r in results:
    print('--- ', len(str(r)))
print("=== Time taken: {}".format(time.time() - start_time))

# V2
print('=== ThreadPool')
start_time = time.time()
pool = ThreadPool(4)
# Open the urls in their own threads
# and return the results
results = pool.map(powpow, payload)
# close the pool and wait for the work to finish
pool.close()
pool.join()
for r in results:
    print('--- ', len(str(r)))
print("=== Time taken: {}".format(time.time() - start_time))

# V3
print('=== Single thread')
start_time = time.time()
for xy in payload:
    r = powpow(xy)
    print('--- ', len(str(r)))
print("=== Time taken: {}".format(time.time() - start_time))
