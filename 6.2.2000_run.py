import time


def timer(function, *args, **kwargs):
    start_time = time.time()
    my_list = list(function(*args, **kwargs))
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time


if __name__ == "__main__":
    print(timer(zip, [1, 2, 3], [4, 5, 6]))


