import math


def combinationsCount(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

def placementsCount(n, k):
    return math.factorial(n) / math.factorial(n - k)

"""
w - width [1, 12]
h - height [1, 12]
s - number of states [2, 20]
"""
def answer(w, h, s):
    # number of all matrices is s ** (w * h)

    # Use Burnside's lemma

    rowsSwappingCount = combinationsCount(h, 2)
    columnsSwappingCount = combinationsCount(w, 2)
    rowsAndColumnsSwappingCount = 0
    for i in range(rowsSwappingCount + columnsSwappingCount):
        rowsAndColumnsSwappingCount += combinationsCount(rowsSwappingCount + columnsSwappingCount, i + 1)

    actionsCount = 1 + rowsSwappingCount + columnsSwappingCount + rowsAndColumnsSwappingCount

    result = 0
    # combinations which just do nothing
    result += s ** (w * h)

    # swapping any two rows
    result += rowsSwappingCount * (s ** w)
    # swapping any two columns
    result += columnsSwappingCount * (s ** h)
    # swapping rows and columns
    for i in range(rowsAndColumnsSwappingCount):
        result += 293

    return "elements: {}; actions: {}; result: {};".format(result, actionsCount, result / actionsCount)


    # result = 1 / (math.factorial(w) * math.factorial(h))
    #
    # s = 0
    # for y in range(h):
    #     for x in range(w):
    #         s += 0
    #
    # result *= s
    #
    # return result


    # cartesianProduct = []
    # for y in range(h):
    #     row = []
    #     for x in range(w):
    #         row.append((y, x))
    #     cartesianProduct.append(row)
    #
    # for row in cartesianProduct:
    #     print(row)


    # rowVariants = []
    #
    # # number of nested cycles is equal to w
    # for i in range(s):
    #     for j in range(s):
    #         rowVariants.append((i, j))

    matrixVariants = []



    # return str(len(matricesHashes))


if __name__ == "__main__":
    print(answer(2, 3, 4))
