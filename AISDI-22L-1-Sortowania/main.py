import sys
from algorithms import bubble_sort, selection_sort, merge_sort, quick_sort
from reader import prepare_text
from time_testing import test_time


sys.setrecursionlimit(10000)
text = prepare_text("pan-tadeusz-unix.txt", 10000)


def is_sorted(array):
    """
    Returns True if the array is sorted, False if not
    """
    for element1, element2 in zip(array[:-1], array[1:]):
        if element1 > element2:
            return False
    return True


def fill_table(sorting_algorithm, number_of_entries):
    times_array = []
    for size in range(1, number_of_entries + 1):
        total_time, sorted_text = test_time(
            sorting_algorithm, text[:size * 1000]
        )
        assert is_sorted(sorted_text)
        times_array.append(total_time)
    return times_array


entries = 10

bubble_times = fill_table(bubble_sort, entries)
selection_times = fill_table(selection_sort, entries)
merge_times = fill_table(merge_sort, entries)
quick_times = fill_table(quick_sort, entries)


print(bubble_times)
print(selection_times)
print(merge_times)
print(quick_times)
