from heaps import insert, insert_list, extract
from random import randint, gauss


def check_heap(heap: list, index: int, dim: int):
    first = dim * (index - 1) + 2
    for i in range(dim):
        if first + i < len(heap):
            assert heap[first + i] < heap[index]
            check_heap(heap, first + i, dim)


def test_2ary_insert_range():
    values = list(range(1000))
    heap = [None]
    for val in values:
        insert(heap, val, 2)
        check_heap(heap, 1, 2)


def test_2ary_insert_random():
    values = [randint(0, 2000) for _ in range(1000)]
    heap = [None]
    for val in values:
        insert(heap, val, 2)
        check_heap(heap, 1, 2)


def test_2ary_insert_gauss():
    values = [gauss(1000, 500) for _ in range(1000)]
    heap = [None]
    for val in values:
        insert(heap, val, 2)
        check_heap(heap, 1, 2)


def test_2ary_extract_range():
    values = list(range(1000))
    heap = [None]
    insert_list(heap, values, 2)
    for val in values:
        extract(heap, val, 2)
        check_heap(heap, 1, 2)


def test_2ary_extract_random():
    values = [randint(0, 2000) for _ in range(1000)]
    heap = [None]
    for val in values:
        insert(heap, val, 2)
        check_heap(heap, 1, 2)


def test_2ary_extract_gauss():
    values = [gauss(1000, 500) for _ in range(1000)]
    heap = [None]
    for val in values:
        insert(heap, val, 2)
        check_heap(heap, 1, 2)


def test_3ary_insert_range():
    values = list(range(1000))
    heap = [None]
    for val in values:
        insert(heap, val, 3)
        check_heap(heap, 1, 3)


def test_3ary_insert_random():
    values = [randint(0, 2000) for _ in range(1000)]
    heap = [None]
    for val in values:
        insert(heap, val, 3)
        check_heap(heap, 1, 3)


def test_3ary_insert_gauss():
    values = [gauss(1000, 500) for _ in range(1000)]
    heap = [None]
    for val in values:
        insert(heap, val, 3)
        check_heap(heap, 1, 3)


def test_4ary_insert_range():
    values = list(range(1000))
    heap = [None]
    for val in values:
        insert(heap, val, 4)
        check_heap(heap, 1, 4)


def test_4ary_insert_random():
    values = [randint(0, 2000) for _ in range(1000)]
    heap = [None]
    for val in values:
        insert(heap, val, 4)
        check_heap(heap, 1, 4)


def test_4ary_insert_gauss():
    values = [gauss(1000, 500) for _ in range(1000)]
    heap = [None]
    for val in values:
        insert(heap, val, 4)
        check_heap(heap, 1, 4)
