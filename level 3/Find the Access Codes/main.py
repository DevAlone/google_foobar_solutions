import math


def answer(l):
    result = 0
    number_of_doubles = [0 for _ in l]
    for i in range(1, len(l) - 1):
        for j in range(0, i):
            if l[i] % l[j] == 0:
                number_of_doubles[i] += 1

    for i in range(2, len(l)):
        for j in range(1, i):
            if l[i] % l[j] == 0:
                result += number_of_doubles[j]

    return result

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6]
    data = [i for i in range(1, 1000)]
    result = answer(data)
    print(result)

