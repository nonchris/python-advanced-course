import sys
import time

import numpy as np

# https://gist.github.com/nonchris/0e35a5999f6aed82680bac32ab02084c

"""
Just a quick non scientific performance test for iterables from python and numpy.
This is only meant to get a rough feeling for different performances.
"""


def test_speed(array):
    """
    Takes an iterable and measures the time it takes to iterate over the array in different ways

    :param: list, numpy array or other iterable
    """
    print(f"running tests type: {type(array)} with {len(array)} entries")

    # for in range
    start = time.time()
    for i in range(len(array)):
        array[i] = array[i] + 1

    t2 = time.time()

    print(f"ran for in range      {t2 - start}")

    # ----------

    # for enumerate
    start = time.time()
    for i, elm in enumerate(array):
        array[i] = elm + 1

    t2 = time.time()
    print(f"ran for in enum       {t2 - start}")

    # ----------

    # comprehension
    start = time.time()
    a_2 = [e + 1 for e in array]
    t2 = time.time()
    print(f"ran comprehension     {t2 - start}")

    # ----------

    # while
    start = time.time()
    i = 0
    while i < len(array):
        array[i] = array[i] + 1
        i += 1

    t2 = time.time()
    print(f"ran while loop        {t2 - start}")

    # ----------

    # recursion?
    # I tried but then I realized that this is python
    # default recursion depth 1k you can adjust it
    # but it won't let you do crazy stuff like 20k

    # ----------

    # do type specific things list
    if type(array) is list:
        start = time.time()
        a_2 = np.array(array)
        t2 = time.time()
        print(f"conversion np.array   {t2 - start}")

    # ----------

    # type specific numpy
    if type(array) is np.ndarray:

        start = time.time()
        a_2 = list(array)
        t2 = time.time()
        print(f"conversion list:      {t2 - start}")

        start = time.time()
        array += array + 1
        t2 = time.time()
        print(f"ran numpy internal    {t2 - start}")


if __name__ == "__main__":
    # python list
    array = [i for i in range(2000000)]
    test_speed(array)

    print()

    # numpy array
    array = np.arange(0, 2000000)
    test_speed(array)
