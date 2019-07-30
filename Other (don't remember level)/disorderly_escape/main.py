import math


# def getMatrixHash(matrix):
#     rowsHash = []
#     columnsHash = []
#     for row in matrix:
#         rowsHash.append(sum(row))
#
#     for x in range(len(matrix[0])):
#         columnSum = 0
#         for y in range(len(matrix)):
#             columnSum += matrix[y][x]
#             columnsHash.append(columnSum)
#     rowsHash.sort()
#     columnsHash.sort()
#     matrixHash = 0
#     for val in rowsHash:
#         matrixHash <<= 32
#         matrixHash |= val
#     for val in columnsHash:
#         matrixHash <<= 32
#         matrixHash |= val
#
#     return matrixHash


# class MatricesCombinations:
#     def __init__(self, width, height, elementRange):
#         self.width = width
#         self.height = height
#         self.elementRange = elementRange
#         self.matricesHashes = Set()

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
    # rowsAndColumnsSwappingCount = math.factorial(rowsSwappingCount) * math.factorial(columnsSwappingCount)
    rowsAndColumnsSwappingCount = 0
    for i in range(rowsSwappingCount + columnsSwappingCount):
        rowsAndColumnsSwappingCount += combinationsCount(rowsSwappingCount + columnsSwappingCount, i + 1)

    actionsCount = 1 + rowsSwappingCount + columnsSwappingCount + rowsAndColumnsSwappingCount

    result = 0
    # combinations which just do nothing
    result += s ** (w * h)
    # result += combinationsCount(s ** w, h)
    # result += placementsCount(s ** w, h)

    # swapping any two rows
    result += rowsSwappingCount * (s ** w)
    # swapping any two columns
    result += columnsSwappingCount * (s ** h)
    # swapping rows and columns
    # result += 4  # rowsSwappingCount * columnsSwappingCount * s
    # result += (rowsSwappingCount + columnsSwappingCount) * (rowsSwappingCount * (s ** w) - 2 + columnsSwappingCount * (s ** h) - 2)
    # result += 4

    # for y in range(rowsSwappingCount):
    #     for x in range(columnsSwappingCount):
    #         result += 174  # 4 + 4 * 4  # (s ** (w - 2)) + (s ** (h - 2)) + 2
    for i in range(rowsAndColumnsSwappingCount):
        result += 293

    #
    # result = 3440

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