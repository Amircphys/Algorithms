import pytest
from sort_functions import (
    sort_by_insert,
    sort_bubble,
    sort_selection,
    merge,
    sort_merge,
    sort_quick,
)

TEST_DATA = [
    ([], []),
    ([1], [1]),
    ([1, 2, 3], [1, 2, 3]),
    ([1, 1, 1], [1, 1, 1]),
    ([2, 1, 0], [0, 1, 2]),
    ([1, -1], [-1, 1]),
    ([0, 1, 2, -1], [-1, 0, 1, 2]),
    ([1, 0, 2, -1, 3, -2], [-2, -1, 0, 1, 2, 3]),
    ([1, 1, 2, 0], [0, 1, 1, 2]),
    ([-1, -1, -2, 0], [-2, -1, -1, 0]),
]

SORT_FUNCTIONS = [sort_by_insert, sort_bubble, sort_selection, sort_merge, sort_quick]


@pytest.mark.parametrize("func", SORT_FUNCTIONS)
@pytest.mark.parametrize("inp,exp_out", TEST_DATA)
def test_sort_functions(func, inp, exp_out):
    result = func(inp)
    assert (
        result == exp_out
    ), f"Ошибка в {func.__name__}: вход {inp}, ожидалось {exp_out}, получено {result}"


@pytest.mark.parametrize(
    "array_left,array_right,expected_result",
    [
        ([1, 2, 3], [], [1, 2, 3]),
        ([], [1, 2, 3], [1, 2, 3]),
        ([1, 2, 3], [3, 4, 5], [1, 2, 3, 3, 4, 5]),
        ([1, 2, 3], [-1, 4, 5], [-1, 1, 2, 3, 4, 5]),
        ([1, 2, 3], [-4, -1, 0], [-4, -1, 0, 1, 2, 3]),
    ],
)
def test_merge(array_left, array_right, expected_result):
    result = merge(array_left, array_right)
    assert (
        result == expected_result
    ), f"Ошибка при слиянии: вход ({array_left}, {array_right}), ожидалось {expected_result}, получено {result}"
