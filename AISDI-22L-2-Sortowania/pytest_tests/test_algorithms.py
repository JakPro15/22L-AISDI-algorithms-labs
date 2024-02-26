import random
from ..sources.algorithms import (
    bubble_sort,
    selection_sort,
    merge_sort,
    quick_sort
)


def generate_table(randomizer, size=10000):
    table = []
    for _ in range(size):
        table.append(randomizer())
    return table


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
    table = bubble_sort(table)
    assert is_sorted(table)


def test_bubble_sort_gauss_table():
    table = generate_table(lambda: random.gauss(1000, 100), 500)
    table = bubble_sort(table)
    assert is_sorted(table)


def test_bubble_sort_sorted_table():
    table = list(range(800))
    table = bubble_sort(table)
    assert is_sorted(table)


def test_selection_sort_random_table():
    table = generate_table(lambda: random.randint(0, 10000), 600)
    table = selection_sort(table)
    assert is_sorted(table)


def test_selection_sort_gauss_table():
    table = generate_table(lambda: random.gauss(1000, 100), 500)
    table = selection_sort(table)
    assert is_sorted(table)


def test_selection_sort_sorted_table():
    table = list(range(800))
    table = selection_sort(table)
    assert is_sorted(table)


def test_merge_sort_random_table():
    table = generate_table(lambda: random.randint(0, 10000), 600)
    table = merge_sort(table)
    assert is_sorted(table)


def test_merge_sort_gauss_table():
    table = generate_table(lambda: random.gauss(1000, 100), 500)
    table = merge_sort(table)
    assert is_sorted(table)


def test_merge_sort_sorted_table():
    table = list(range(800))
    table = merge_sort(table)
    assert is_sorted(table)


def test_quick_sort_random_table():
    table = generate_table(lambda: random.randint(0, 10000), 600)
    table = quick_sort(table)
    assert is_sorted(table)


def test_quick_sort_gauss_table():
    table = generate_table(lambda: random.gauss(1000, 100), 500)
    table = quick_sort(table)
    assert is_sorted(table)


def test_quick_sort_sorted_table():
    table = list(range(800))
    table = quick_sort(table)
    assert is_sorted(table)
