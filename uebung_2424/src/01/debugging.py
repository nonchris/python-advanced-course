import random

def sort_1(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n - i - 2):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


def sort_2(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[min_index] > lst[i]:
                min_index = i
            lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst


def sort_3(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j] = key
    return lst

def fibonacci(n):
    if n <= 0:
        return "Input should be positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n)


if __name__ == '__main__':
    random.seed(42)  # use seed to have reproducible outputs
    numbers = [round(random.random() * 100, 4) for i in range(20)]

    truth = sorted(numbers.copy())
    print(f"{'truth:': <7} {truth}")

    # TODO: fix those sorting algorithms
    res_1 = sort_1(numbers.copy())
    res_2 = sort_2(numbers.copy())
    res_3 = sort_3(numbers.copy())

    print(f"{'sort_1:': <7} {res_1}")
    print(f"{'sort_2:': <7} {res_2}")
    print(f"{'sort_3:': <7} {res_3}")

    print()

    # TODO: why does this raise an recursion error??
    # res_4 = ", ".join(str(fibonacci(i)) for i in range(10))  # expected: 0, 1, 1, 2, 3, 5, 8, 13, 21
    # print(res_4)

