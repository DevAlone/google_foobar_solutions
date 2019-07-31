import copy

DEBUG = False


def to_boolean_array(array):
    # just to make the literals more readable
    return [bool(x) for x in array]


def to_boolean_matrix(matrix):
    # just to make the literals more readable
    return [to_boolean_array(row) for row in matrix]


expanding_rules = {
    True: [to_boolean_array(x) for x in [
        [1, 0,
         0, 0],
        [0, 1,
         0, 0],
        [0, 0,
         1, 0],
        [0, 0,
         0, 1],
    ]],
    False: [to_boolean_array(x) for x in [
        # 0
        [0, 0,
         0, 0],
        # 2
        [1, 1,
         0, 0],
        [1, 0,
         1, 0],
        [1, 0,
         0, 1],
        [0, 1,
         1, 0],
        [0, 1,
         0, 1],
        [0, 0,
         1, 1],
        # 3
        [1, 1,
         1, 0],
        [1, 1,
         0, 1],
        [1, 0,
         1, 1],
        [0, 1,
         1, 1],
        # 4
        [1, 1,
         1, 1],
    ]],
}


def matrix_to_str(matrix):
    result = '[\n'
    for row in matrix:
        result += '\t[' + ', '.join([
            str(int(x) if x is not None else None) for x in row
        ]) + '],\n'
    result += ']'

    return result


def can_be_converted(expanded_matrix, matrix):
    height = len(expanded_matrix)
    width = len(expanded_matrix[0])

    result = [[None for _ in range(width - 1)] for _ in range(height - 1)]

    for y in range(height - 1):
        for x in range(width - 1):
            number_of_ones = int(expanded_matrix[y][x])
            number_of_ones += int(expanded_matrix[y][x + 1])
            number_of_ones += int(expanded_matrix[y + 1][x])
            number_of_ones += int(expanded_matrix[y + 1][x + 1])

            result[y][x] = True if number_of_ones == 1 else False

    return result == matrix


def count_combinations(matrix, expanded_matrix, curr_index, store_result_matrices=None):
    height = len(matrix)
    width = len(matrix[0])

    if curr_index >= height * width:
        if can_be_converted(expanded_matrix, matrix):
            if type(store_result_matrices) is list:
                store_result_matrices.append(expanded_matrix)

            if DEBUG:
                print(matrix_to_str(expanded_matrix), ' -> ', matrix_to_str(matrix))
                input('press enter')

            return 1

        return 0

    y = curr_index // width
    x = curr_index % width

    expansions = expanding_rules[matrix[y][x]]

    result = 0

    for expansion in expansions:
        new_expanded_matrix = copy.deepcopy(expanded_matrix)

        # check if it fits with already placed elements and place new one
        def set_if_fits(y, x, expansion_index):
            if new_expanded_matrix[y][x] is None:
                new_expanded_matrix[y][x] = expansion[expansion_index]
                return True

            return new_expanded_matrix[y][x] == expansion[expansion_index]

        if not set_if_fits(y, x, 0):
            continue

        if not set_if_fits(y, x + 1, 1):
            continue

        if not set_if_fits(y + 1, x, 2):
            continue

        if not set_if_fits(y + 1, x + 1, 3):
            continue

        if DEBUG:
            print('path: ', matrix_to_str(new_expanded_matrix), ' -> ', matrix_to_str(matrix))

        result += count_combinations(matrix, new_expanded_matrix, curr_index + 1, store_result_matrices)

    return result


def solution(matrix, store_result_matrices=None):
    height = len(matrix)
    width = len(matrix[0])

    return count_combinations(
        matrix,
        [[None for _ in range(width + 1)] for _ in range(height + 1)],
        0,
        store_result_matrices,
    )


def get_transponsed_matrix(m):
    transposed = []
    height = len(m)
    width = len(m[0])

    for x in range(width):
        row = []
        for y in range(height):
            row.append(m[y][x])

        transposed.append(row)

    return transposed


if __name__ == '__main__':
    def test(matrix, is_printed=True, store_result_matrices=None):
        a = solution(to_boolean_matrix(matrix), store_result_matrices)
        if is_printed:
            print(a)

        return a

    matrices = []
    test([
        [1, 0, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [1, 0, 1, 0, 1],
    ], True, matrices)


    for matrix in matrices:
        print(matrix_to_str(matrix))

    exit(1)
    m = [[True, True, False, True, False, True, False, True, True, False],
              [True, True, False, False, False, False, True, True, True, False],
              [True, True, False, False, False, False, False, False, False, True],
              [False, True, False, False, False, False, True, True, False, False]]
    print(matrix_to_str(m))
    print(matrix_to_str(get_transponsed_matrix(m)))

    solution(get_transponsed_matrix([[True, True, False, True, False, True, False, True, True, False],
              [True, True, False, False, False, False, True, True, True, False],
              [True, True, False, False, False, False, False, False, False, True],
              [False, True, False, False, False, False, True, True, False, False]]))

    '''
    solution([[True, True, False, True, False, True, False, True, True, False],
              [True, True, False, False, False, False, True, True, True, False],
              [True, True, False, False, False, False, False, False, False, True],
              [False, True, False, False, False, False, True, True, False, False]])
    '''

    exit(1)



    matrices = []

    for i in range(1, 18):
        print(i, end=': ')
        print([1 for _ in range(i)], end='; ')
        test([
            [1 for _ in range(i)],
        ], True, matrices)

    for matrix in matrices:
        pass
        # print(matrix_to_str(matrix))

    exit(1)
    test([
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1],
    ])
    exit(1)

    '''
    test([[        0]])
    test([[1]])
    print()

    test([[0, 0]])
    test([[0, 1]])
    test([[1, 0]])
    test([[1, 1]])
    print()
'''

    f = []
    for i in range(32):
        m = []
        buffer = []
        for bit in range(4):
            buffer.append((i >> bit) & 1)
            if len(buffer) >= 2:
                m.append(buffer)
                buffer = []

        # print(matrix_to_str(m))
        r = solution(to_boolean_matrix(m))
        f.append((m, r))
        # test(m)

    f = sorted(f, key=lambda x: x[1])
    print()
    # print(f)

    for item in f:
        print(item[1], matrix_to_str(item[0]))

    exit(0)
    print(solution(to_boolean_matrix([
        [1, 0],
        [0, 1]
    ])))
    print(solution([[True, False, True], [False, True, False], [True, False, True]]))
    print(solution(
        [[True, False, True, False, False, True, True, True], [True, False, True, False, False, False, True, False],
         [True, True, True, False, False, False, True, False], [True, False, True, False, False, False, True, False],
         [True, False, True, False, False, True, True, True]]))
    print(solution([[True, True, False, True, False, True, False, True, True, False],
                    [True, True, False, False, False, False, True, True, True, False],
                    [True, True, False, False, False, False, False, False, False, True],
                    [False, True, False, False, False, False, True, True, False, False]]))
