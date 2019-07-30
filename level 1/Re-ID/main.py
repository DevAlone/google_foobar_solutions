import math

import sys


prime_string = ""
MIN_PRIME_NUMBERS_CACHE = 10000
ID_SIZE = 5
MAGIC_NUMBER = 2.5


def sieve_of_eratosthenes(n):
    if n < 2:
        raise ValueError()

    values = [True for _ in range(n - 2)]

    for i in range(2, int(round(math.sqrt(n)))):
        if values[i - 2]:
            for k in range(i*i, n, i):
                values[k - 2] = False

    return [i + 2 for i, x in enumerate(values) if x]


def get_prime_string(n):
    return ''.join((str(x) for x in sieve_of_eratosthenes(n)))


def answer(n):
    global prime_string
    if not prime_string or n > len(prime_string) - ID_SIZE:
        prime_string = get_prime_string(max(int(n * MAGIC_NUMBER), MIN_PRIME_NUMBERS_CACHE))

    return prime_string[n:n + ID_SIZE]


if __name__ == '__main__':
    result = answer(int(sys.argv[1]))
    print(result)
