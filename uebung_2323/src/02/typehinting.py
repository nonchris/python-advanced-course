from typing import Literal, Callable


def slc(s, i):
    return list(s[::i])

def transform_to_dict(a_list):
    return {k: v for k, v in a_list}

def times_n(elm, factor):
    return elm * factor

def apply(data, fn, factor=2):
    r =  {str(fn(elm, factor)) for elm in data}
    return r if len(r) % 2 else None


if __name__ == '__main__':

    res = slc("abcde", 2)
    print(res)

    d = [("a", 64), ("b", 69), ("c", 42)]
    res = transform_to_dict(d)
    print(res)

    d = ["brrrr", 2, 3.5, ("bbbbeeee", 2), 2]
    res = apply(d, times_n)
    print(res)

    # assign these variables a value that fulfills the typehints
    l: list[str, int, dict[str, Literal["nice", "doof"]]]

    c: Callable[[str, int], list[str]]
