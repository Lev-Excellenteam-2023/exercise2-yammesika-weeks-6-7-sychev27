import time


def timer(f, *args, **kwargs):
    st = time.time()
    n = list(f(*args, **kwargs))
    et = time.time()
    elapsed_time = et - st
    return elapsed_time


print(timer(zip, [1, 2, 3], [4, 5, 6]))


