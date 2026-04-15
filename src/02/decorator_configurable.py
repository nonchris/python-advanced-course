from typing import Callable


# this function gets evaluated 'normally_
def call_me_n_times(n: int) -> Callable:

    # this is the actual decorator that is created
    def actual_decorator(old_function: Callable) -> Callable:

        # the decorator will be resolved to be this new function
        def new_function(*args, **kwargs):
            for i in range(n):
                old_function(*args, **kwargs)

        return new_function

    return actual_decorator

@call_me_n_times(3)
def say_thing(thing: str):
    print(thing)


if __name__ == '__main__':
    say_thing("hello!")
