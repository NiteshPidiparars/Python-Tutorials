from functools import lru_cache
import time


@lru_cache(maxsize=4)
def myfunc(x):
    time.sleep(2)
    return x


myfunc(1)
# myfunc(1) takes 2 seconds and results for myfunc(1) are now cached
myfunc(1)
myfunc(2)
myfunc(3)
myfunc(4)
myfunc(5)


@lru_cache(maxsize=32)
def some_work(n):
    # Some task taking n seconds
    time.sleep(n)
    return n


if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    some_work(1)
    some_work(6)
    some_work(2)
    print("Done... Calling again")
    input()
    some_work(3)
    print("Called again")
