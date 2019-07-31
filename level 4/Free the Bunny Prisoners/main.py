import itertools

"""
num_buns - bunnies I have [1, 9]
num_required - bunnies required to open one door [0, 9]
"""
def answer(num_buns, num_required):
    if num_buns < num_required:
        raise Exception('Oh no, we are DOOMED! There are too few bunnies!')

    # get minimum combination such that we wouldn't give more keys
    # than necessary to open any door by any num_required bunnies
    num_required = num_buns - num_required + 1

    bunnies = []

    # just create bunnies
    for i in range(num_buns):
        bunnies.append([])

    keysCombinations = \
        list(itertools.combinations(range(num_buns), num_required))
    combinationsCount = len(keysCombinations)

    for i in range(combinationsCount):
        for bunnyIndex in keysCombinations[i]:
            bunnies[bunnyIndex].append(i)

    return bunnies


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print('Use it like this: \n\t\tprogram num_buns num_required')
        exit(1)

    print(answer(int(sys.argv[1]), int(sys.argv[2])))

