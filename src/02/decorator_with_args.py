from typing import Callable

def call_me_twice(old_function: Callable) -> Callable:
    # this function needs to match the signature of the original one
    # we can just make it fully dynamic by just using args and kwargs here
    def new_function(*args, **kwargs):
        old_function(*args, **kwargs)
        old_function(*args, **kwargs)

    return new_function

@call_me_twice
def say_thing(thing: str):
    print(thing)

if __name__ == '__main__':

    say_thing("hello!")
