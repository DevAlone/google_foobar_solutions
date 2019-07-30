def answer(M, F):
    # some optimizations
    if (M > 1 and M == F) or \
       (F > 1 and M % F == 0) or \
       (M > 1 and F % M == 0):
        return "impossible"

    cycles = 0
    while M > 1 or F > 1:
        if M > F:
            M -= F
        else:
            F -= M
        cycles += 1
        if M < 1 or F < 1:
            break

    if M < 1 or F < 1:
        return "impossible"

    return str(cycles)


def answer1(M, F):
    cycles = 0
    while M > 1 or F > 1:
        minVal = min(M, F)
        maxVal = max(M, F)

        c = (maxVal - minVal) // minVal
        if c < 1:
            c = 1

        if M > F:
            M -= c * minVal
        else:
            F -= c * minVal

        cycles += c
        if M < 1 or F < 1:
            return "impossible"

    return str(cycles)


def test():
    N = 10
    for i in range(1, N):
        for j in range(1, N):
            print('{} {}: {}'.format(i, j, answer(i, j)))


if __name__ == "__main__":
    test()
