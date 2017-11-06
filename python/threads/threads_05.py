import time
from multiprocessing import Pool
from concurrent.futures import ProcessPoolExecutor


def calc(xy):
    x, y = xy
    res = pow(x, y)
    print(len(str(res)))


if __name__ == '__main__':
    payload = [(x, 123451) for x in range(320, 330)]

    # V1
    start_time = time.time()
    for xy in payload:
        calc(xy)
    print("=== Time taken: {}".format(time.time() - start_time))

    # V2
    start_time = time.time()
    pool = Pool(3)
    pool.map(calc, payload)
    pool.close()
    pool.join()
    print("=== Time taken: {}".format(time.time() - start_time))

    start_time = time.time()
    with ProcessPoolExecutor(max_workers=3) as executor:
        executor.map(calc, payload)
    print("=== Time taken: {}".format(time.time() - start_time))
