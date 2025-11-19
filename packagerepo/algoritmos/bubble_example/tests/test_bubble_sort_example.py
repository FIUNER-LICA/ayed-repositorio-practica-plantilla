import random
import pytest

from packagerepo.algoritmos.bubble_example.implementation import bubble_sort

def test_empty_list():
    assert bubble_sort([]) == []

def test_single_element():
    assert bubble_sort([42]) == [42]

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([3, 1, 2, 1, 3], [1, 1, 2, 3, 3]),
    ([0, -1, 5, -10, 3], [-10, -1, 0, 3, 5]),
])
def test_various_lists(input_list, expected):
    assert bubble_sort(input_list) == expected

def test_random_lists():
    random.seed(0)
    for _ in range(100):
        size = random.randint(0, 20)
        lst = [random.randint(-100, 100) for _ in range(size)]
        assert bubble_sort(lst) == sorted(lst)

def test_does_not_modify_original():
    original = [3, 2, 1]
    copy = original.copy()
    _ = bubble_sort(original)
    assert original == copy  # ensure the input list was not mutated