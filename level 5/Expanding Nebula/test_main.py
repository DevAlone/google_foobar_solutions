from main_slow import solution as slow_solution
from main import *


def test_can_be_converted():
    from_matrix = to_boolean_matrix([
        [1, 0, 0, 1],
        [0, 0, 0, 0],
    ])
    to_matrix = to_boolean_matrix([
        [1, 0, 1],
    ])

    assert can_be_converted(from_matrix, to_matrix)

    from_matrix = to_boolean_matrix([
        [1, 0, 0, 1],
        [0, 0, 0, 1],
    ])
    to_matrix = to_boolean_matrix([
        [1, 0, 1],
    ])

    assert not can_be_converted(from_matrix, to_matrix)


def test_number_to_bit_array():
    assert number_to_bit_array(5) == [1, 0, 1]
    assert number_to_bit_array(6) == [1, 1, 0]
    assert bit_array_to_number([1, 0, 1, 1, 1, 1, 0]) == 94
    assert bit_array_to_number([0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0]) == bit_array_to_number([1, 0, 1, 1, 1, 1, 0])
    array = number_to_bit_array(517)
    assert bit_array_to_number(array) == 517

    for i in range(255):
        array = number_to_bit_array(i)
        assert bit_array_to_number(array) == i

    for i in range(255):
        array = number_to_bit_array(i, 100)
        assert len(array) == 100
        assert bit_array_to_number(array) == i


def test_correctness_slow_solution():
    assert slow_solution(to_boolean_matrix([
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1],
    ])) == 4

    '''
    assert slow_solution([
        [True, False, True, False, False, True, True, True],
        [True, False, True, False, False, False, True, False],
        [True, True, True, False, False, False, True, False],
        [True, False, True, False, False, False, True, False],
        [True, False, True, False, False, True, True, True]
    ]) == 254
    '''


def test_correctness_fast_solution():
    assert solution(to_boolean_matrix([
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1],
    ])) == 4

    assert solution([
        [True, False, True, False, False, True, True, True],
        [True, False, True, False, False, False, True, False],
        [True, True, True, False, False, False, True, False],
        [True, False, True, False, False, False, True, False],
        [True, False, True, False, False, True, True, True]
    ]) == 254

    assert solution([
        [True, True, False, True, False, True, False, True, True, False],
        [True, True, False, False, False, False, True, True, True, False],
        [True, True, False, False, False, False, False, False, False, True],
        [False, True, False, False, False, False, True, True, False, False]
    ]) == 11567
