import math
import functools


def memoization(func):
    _cache = {}
    @functools.wraps(func)
    def wrapper(argument):
        if argument not in _cache:
            _cache[argument] = func(argument)
        return _cache[argument]

    return wrapper


@memoization
def sum_of_odd_divisors(n):
    return sum([
        i if n / i == i else i + n / i
        for i in range(1, int(math.sqrt(n) + 1)) if n % i == 0
    ])


@memoization
def distinct_partitions_number(n):
    if n == 0 or n == 1:
        return 1

    def s(n):
        if n % 1 == 0:
            return sum_of_odd_divisors(float(n))
        else:
            return 0

    return int(sum([
        (s(k) - 2 * s(k / 2.0)) * distinct_partitions_number(n - k)
        for k in range(1, n + 1)
    ]) / n)


def answer(n):
    return distinct_partitions_number(n) - 1


if __name__ == '__main__':
    for i in range(1, 11):
        print("{}:\t\t{}".format(i, answer(i)))
