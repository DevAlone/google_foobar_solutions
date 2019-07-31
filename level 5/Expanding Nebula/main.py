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
    from_height = len(expanded_matrix)
    from_width = len(expanded_matrix[0])
    to_height = len(matrix)
    to_width = len(matrix[0])
    if from_height != to_height + 1 or from_width != to_width + 1:
        return False

    result = [[None for _ in range(from_width - 1)] for _ in range(from_height - 1)]

    for y in range(from_height - 1):
        for x in range(from_width - 1):
            number_of_ones = int(expanded_matrix[y][x])
            number_of_ones += int(expanded_matrix[y][x + 1])
            number_of_ones += int(expanded_matrix[y + 1][x])
            number_of_ones += int(expanded_matrix[y + 1][x + 1])

            result[y][x] = True if number_of_ones == 1 else False

    return result == matrix


def bit_array_to_number(array):
    """
    converts array of bits(True, False, or 0, 1) to the number

    :param array:
    :return:
    """

    result = 0
    for i, item in enumerate(reversed(array)):
        result |= item << i

    return result


def number_to_bit_array(number, minimum_width=0):
    """
    converts number to array of bits(True, False)

    :param number:
    :return:
    """

    result = []
    while number:
        result.append(number & 1)
        number >>= 1

    result = list(reversed(result))

    while len(result) < minimum_width:
        result.insert(0, 0)

    return result


def count_combinations(matrix):
    height = len(matrix)
    width = len(matrix[0])
    if height < 3 or height > 65535 or width < 3 or width > 65535:
        raise ValueError("wrong input")

    previous_row_combinations = {}

    def get_window_matrices(row_to_expand, previous_state, current_index=0):
        """
        returns every possible window matrix for the given arguments
        :param row_to_expand: row from matrix to expand
        :param previous_state: previous state of our expanded matrix
        :param current_index: index in row_to_expand
        where only None elements can be filled with new values
        """
        if current_index >= width:
            # return filled matrix
            if can_be_converted(previous_state, [row_to_expand]):
                yield previous_state
            return

        expansions = expanding_rules[row_to_expand[current_index]]

        for expansion in expansions:
            new_expanded_window = copy.deepcopy(previous_state)

            def set_if_fits(y, x, expansion_index):
                """
                check if new expansion fits with already placed elements and set if so
                :param y: index in expanded window matrix
                :param x: index in expanded window matrix
                :param expansion_index: index of element in expansion
                :return:
                """
                if new_expanded_window[y][x] is None:
                    new_expanded_window[y][x] = expansion[expansion_index]
                    return True

                return new_expanded_window[y][x] == expansion[expansion_index]

            # skip if some expansion does not fit
            if not set_if_fits(0, current_index, 0):
                continue
            if not set_if_fits(0, current_index + 1, 1):
                continue
            if not set_if_fits(1, current_index, 2):
                continue
            if not set_if_fits(1, current_index + 1, 3):
                continue

            for x in get_window_matrices(row_to_expand, new_expanded_window, current_index + 1):
                yield x

    for row in matrix:
        if len(previous_row_combinations):
            # if we have constraints from the previous step
            next_row_combinations = {}
            for previous_row_number, number_of_combinations in previous_row_combinations.items():
                previous_row = number_to_bit_array(previous_row_number, width + 1)
                prev_state = [
                    previous_row,
                    [None for _ in range(width + 1)]
                ]
                for window_matrix in get_window_matrices(row, prev_state):
                    # number_of_window_matrices += 1
                    window_matrix_number = bit_array_to_number(window_matrix[-1])
                    if window_matrix_number in next_row_combinations:
                        next_row_combinations[window_matrix_number] += number_of_combinations
                    else:
                        next_row_combinations[window_matrix_number] = number_of_combinations

            previous_row_combinations = next_row_combinations
        else:
            for window_matrix in get_window_matrices(row, [[None for _ in range(width + 1)] for _ in range(2)]):
                window_matrix_number = bit_array_to_number(window_matrix[-1])
                if window_matrix_number in previous_row_combinations:
                    previous_row_combinations[window_matrix_number] += 1
                else:
                    previous_row_combinations[window_matrix_number] = 1

    return sum(previous_row_combinations.values())


def solution(matrix):
    height = len(matrix)
    width = len(matrix[0])

    if width > height:
        # transponse so that width <= height
        matrix = get_transponsed_matrix(matrix)

    return count_combinations(
        matrix,
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


def main():
    def test(matrix, is_printed=True):
        a = solution(to_boolean_matrix(matrix))
        if is_printed:
            print(a)

        return a

    test([
        [1, 0, 1],  # , 0, 0],
        [0, 1, 0],  # , 0, 0],
        [1, 0, 1],  # , 0, 1],
    ])

    test([
        [1, 0, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [1, 0, 1, 0, 1],
    ])


if __name__ == '__main__':
    main()
