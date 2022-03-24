import time
import gc
import random
from algorithms import (
    bubble_sort,
    merge_sort,
    selection_sort,
    quick_sort
)


def generate_table(randomizer, size=10000):
    table = []
    for _ in range(size):
        table.append(randomizer())
    return table


def test_time(sort, table):
    gc_old = gc.isenabled()
    gc.disable()

    start_time = time.process_time()
    sorted = sort(table)
    end_time = time.process_time()

    if gc_old:
        gc.enable()

    return end_time - start_time, sorted


def complete_random_test():
    print("Testing sorting of completely random tables")

    table = generate_table(lambda: random.randint(0, 10000))
    print(f"Bubble sort: {test_time(bubble_sort, table.copy())[0]}")
    print(f"Selection sort: {test_time(selection_sort, table.copy())[0]}")
    print(f"Merge sort: {test_time(merge_sort, table.copy())[0]}")
    print(f"Quick sort: {test_time(quick_sort, table.copy())[0]}")


def gauss_test():
    print("Testing sorting of tables with numbers randomized with Gaussian"
          " distribution")

    table = generate_table(lambda: random.gauss(5000, 2000))
    print(f"Bubble sort: {test_time(bubble_sort, table.copy())[0]}")
    print(f"Selection sort: {test_time(selection_sort, table.copy())[0]}")
    print(f"Merge sort: {test_time(merge_sort, table.copy())[0]}")
    print(f"Quick sort: {test_time(quick_sort, table.copy())[0]}")


def sorted_test():
    print("Testing sorting of sorted tables")

    table = list(range(10000))
    print(f"Bubble sort: {test_time(bubble_sort, table.copy())[0]}")
    print(f"Selection sort: {test_time(selection_sort, table.copy())[0]}")
    print(f"Merge sort: {test_time(merge_sort, table.copy())[0]}")
    print(f"Quick sort: {test_time(quick_sort, table.copy())[0]}")


if __name__ == "__main__":
    complete_random_test()
    gauss_test()
    sorted_test()
