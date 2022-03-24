import time
import sys
from algorithms import bubble_sort, selection_sort, merge_sort, quick_sort
from reader import prepare_text
from time_testing import test_time

sys.setrecursionlimit(10000)


def fill_table(sorting_algorithm, number_of_entries):
    times_array = []
    for size in range(1, number_of_entries + 1):
        text = prepare_text("pan-tadeusz-unix.txt", size * 1000)
        total_time = test_time(text, sorting_algorithm)
        times_array.append(total_time)
    return times_array


entries = 10

bubble_times = fill_table(bubble_sort, entries)
selection_times = fill_table(selection_sort, entries)
merge_times = fill_table(merge_sort, entries)
quick_times = fill_table(quick_sort, entries)
