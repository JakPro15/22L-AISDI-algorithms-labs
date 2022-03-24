import random
from .algorithms import (
    bubble_sort,
    merge_sort,
    selection_sort,
    quick_sort
)
from .time_testing import generate_table


def test_generate_table_1():
    def gen_function():
        return 2

    table = generate_table(gen_function, 456)
    assert len(table) == 456
    for i in range(456):
        assert table[i] == 2


def test_generate_table_2():
    number = [-1]

    def gen_function():
        number[0] += 1
        return number[0]

    table = generate_table(gen_function)
    assert len(table) == 10000
    for i in range(10000):
        assert table[i] == i


def is_sorted(array):
    """
    Returns True if the array is sorted, False if not
    """
    for element1, element2 in zip(array[:-1], array[1:]):
        if element1 > element2:
            return False
    return True


def test_bubble_sort_random_table():
    table = generate_table(lambda: random.randint(0, 10000), 600)
    bubble_sort(table)
    assert is_sorted(table)


def test_bubble_sort_gauss_table():
    table = generate_table(lambda: random.gauss(1000, 100), 500)
    bubble_sort(table)
    assert is_sorted(table)


def test_bubble_sort_sorted_table():
    table = range(800)
    bubble_sort(table)
    assert is_sorted(table)
