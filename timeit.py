import time


def timer(func):
    def wrapper():
        t1 = time.time()
        result = func()
        t2 = time.time()
        print(f'Total time {(t2 - t1)} seconds')
        return result

    return wrapper


@timer
def long_time():
    for i in range(100000):
        for j in range(100):
            i * j


long_time()
