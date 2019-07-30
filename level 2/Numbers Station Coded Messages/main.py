import random


def answer(l, t):
    first_index = 0

    local_sum = 0
    for i, item in enumerate(l):
        local_sum += item

        while local_sum > t and first_index <= i:
            local_sum -= l[first_index]
            first_index += 1

        if local_sum == t:
            return first_index, i

    return -1, -1


def inefficient_answer(l, t):
    for i in range(len(l)):
        local_sum = 0
        for j in range(i, len(l)):
            local_sum += l[j]
            if local_sum == t:
                return i, j
            elif local_sum > t:
                break

    return -1, -1


def generate_random_sequence():
    result = []
    length = random.randint(0, 10)
    for _ in range(length):
        result.append(random.randint(1, 100))

    return result


if __name__ == '__main__':
    while True:
        l = generate_random_sequence()
        t = random.randint(1, 1000)
        result1, result2 = answer(l, t), inefficient_answer(l, t)
        if  result1 != result2:
            print("""
            l = {};
            t = {};
            answer1 = {};
            answer2 = {};
            """.format(l, t, result1, result2))
            break
    # assert answer([4, 3, 10, 2, 8], 12) == (2, 3)
    # assert answer([1, 2, 3, 4], 15) == (-1, -1)
    # assert answer([1, 9, 100, 5, 5, 1], 11) == (3, 5)
    # assert answer([1, 9, 100, 5, 5, 1], 11) == (3, 5)
    # assert answer([1], 11) == (-1, -1)
    # assert answer([15], 15) == (0, 0)
    # assert answer([], 150) == (-1, -1)
    # assert answer([1, 9, 100, 5, 5, 1], 10) == (0, 1)
    # assert answer([1, 9, 100, 5, 5, 1], 6) == (4, 5)
    # assert answer([1, 9, 100, 5, 5, 1], sum([1, 9, 100, 5, 5, 1])) == (0, 5)
    # assert answer([1, 9, 100, 5, 5, 1], 100) == (2, 2)
    # 1 1 5 6 1 9 4: 11
