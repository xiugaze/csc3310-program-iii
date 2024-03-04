import pytest
import random
from quick_select import quick_select


def test_quick_select_single_element():
    array = [5]
    k = 1
    assert quick_select(array, k) == 5


def test_quick_select_multiple_elements():
    array = [9, 3, 7, 1, 5]
    k = 3
    assert quick_select(array, k) == 5


def test_quick_select_negative_numbers():
    array = [-5, -3, -7, -1, -9]
    k = 2
    assert quick_select(array, k) == -7


def test_quick_select_random_elements():
    array = random.sample(range(1, 101), 10)
    k = 7
    assert quick_select(array, k) == sorted(array)[k - 1]


pytest.main()
