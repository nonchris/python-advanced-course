from typing import Iterable, Callable, Literal

numberT = int | float
multiplyT = str | numberT | tuple


def slc(s: str, i: int) -> list[str]:
    return list(s[::i])

def transform_to_dict(a_list: Iterable[tuple[str, numberT]]) -> dict[str, numberT]:
    return {k: v for k, v in a_list}

def times_n(elm: multiplyT, factor: int) -> multiplyT:
    return elm * factor

def apply(data: Iterable[multiplyT], fn: Callable[[multiplyT, int], str], factor: int = 2) -> set[str] | None:
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

    l: list[str, int, dict[str, Literal["nice", "doof"]]] = ["a", 2, {"key": "doof"}]

    c: Callable[[str, int], list[str]]  # ja, das ist absicht, dass die hier einfach slc kopieren könnten :)

