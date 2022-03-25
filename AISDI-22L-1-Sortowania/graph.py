import sys
from algorithms import bubble_sort, selection_sort, merge_sort, quick_sort
from reader import prepare_text
from time_testing import test_time
from matplotlib import pyplot as plt


def is_sorted(array):
    """
    Returns True if the array is sorted, False if not
    """
    for element1, element2 in zip(array[:-1], array[1:]):
        if element1 > element2:
            return False
    return True


def fill_table(sorting_algorithm, number_of_entries, text):
    times_array = []
    for size in range(1, number_of_entries + 1):
        total_time, sorted_text = test_time(
            sorting_algorithm, text[:size * 1000]
        )
        assert is_sorted(sorted_text)
        times_array.append(total_time)
    return times_array


def generate_and_save_graph(text, entries, name, sort_function, color="b"):
    sys.setrecursionlimit(20000)
    times = fill_table(sort_function, entries, text)
    keys = [i * 1000 for i in range(1, entries + 1)]
    plt.plot(
        keys, times, 'o-', label=f"{name} sort", markersize=3, color=color
    )
    plt.legend()
    plt.title(f"{name} sort - time of sorting depending on the length of the"
              " sorted list")
    plt.xlabel("Number of words in the sorted list")
    plt.ylabel("Time of sorting in seconds")
    plt.xticks(keys, [str(element) for element in keys])
    plt.savefig(f"graph_{name.lower()}.png")
    plt.clf()


if __name__ == "__main__":
    text = prepare_text("pan-tadeusz-unix.txt", 10000)
    generate_and_save_graph(text, 10, "Bubble", bubble_sort, "b")
    generate_and_save_graph(text, 10, "Selection", selection_sort, "y")
    generate_and_save_graph(text, 10, "Merge", merge_sort, "g")
    generate_and_save_graph(text, 10, "Quick", quick_sort, "r")
