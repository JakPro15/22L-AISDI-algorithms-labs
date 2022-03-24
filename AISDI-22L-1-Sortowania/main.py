import time
import sys
from algorithms import bubble_sort, selection_sort, merge_sort, quick_sort
from reader import prepare_text

sys.setrecursionlimit(10000)


def fill_table(sorting_algorithm, number_of_entries):
    times_array = []
    for size in range(1, number_of_entries + 1):
        text = prepare_text("pan-tadeusz-unix.txt", size * 1000)
        start_time = time.time()
        if sorting_algorithm == quick_sort:
            quick_sort(text, 0, len(text) - 1)
        else:
            sorting_algorithm(text)
        end_time = time.time()
        total_time = end_time - start_time
        times_array.append(total_time)
    return times_array


entries = 10

bubble_times = fill_table(bubble_sort, entries)
selection_times = fill_table(selection_sort, entries)
merge_times = fill_table(merge_sort, entries)
quick_times = fill_table(quick_sort, entries)
