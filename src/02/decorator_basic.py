from typing import Callable


def call_me_twice(old_function: Callable) -> Callable:

    # note that the inner function makes use of knowing the outer scope!
    def new_function():
        old_function()
        old_function()

    return new_function

@call_me_twice
def say_cyber():
    print("Cyber!")

if __name__ == '__main__':
    say_cyber()
