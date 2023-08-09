import time
from functools import wraps


def show_begin_end(func):
    @wraps(func)
    def deco_func(*args, **kwargs):
        print("== start")
        result = func(*args, **kwargs)
        return result

    return deco_func


@show_begin_end
def sleep_for_a_while():
    print("Sleeping ..")
    time.sleep(2)
    print("Done Sleeping")


sleep_for_a_while()
