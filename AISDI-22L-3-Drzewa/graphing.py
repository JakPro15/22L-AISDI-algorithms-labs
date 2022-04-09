import gc
import time
from matplotlib import pyplot as plt
from bstree import Binary_Search_Tree
from copy import copy


def test_time(process, table):
    gc_old = gc.isenabled()
    gc.disable()

    start_time = time.process_time()
    process(table)
    end_time = time.process_time()

    if gc_old:
        gc.enable()

    return end_time - start_time


def checker(tree_root, min, max):
    if min < tree_root.value < max:
        if not (tree_root.left_tree or tree_root.right_tree):
            return True
        if tree_root.left_tree:
            left = checker(tree_root.left_tree, min, tree_root.value)
        else:
            left = True
        if tree_root.right_tree:
            right = checker(tree_root.right_tree, tree_root.value, max)
        else:
            right = True
        return left and right
    else:
        return False


def fill_table(process, number_of_entries, array):
    times_array = []
    for size in range(1, number_of_entries + 1):
        total_time = test_time(process, array[:size * 1000])
        times_array.append(total_time)
    return times_array


def generate_and_save_graph(array, entries, name, process, color="b"):
    times = fill_table(process, entries, array)
    keys = [i * 1000 for i in range(1, entries + 1)]
    plt.plot(
        keys, times, 'o-', label=f"{name}", markersize=3, color=color
    )
    plt.legend()
    plt.title(f"{name} - time of process depending on the length of the"
              " list")
    plt.xlabel("Number of integers in the array")
    plt.ylabel("Time of sorting in seconds")
    plt.xticks(keys, [str(element) for element in keys])
    plt.savefig(f"graph_{name.lower()}.png")
    plt.clf()


def save_all_graphs(array, tree):
    tree = copy(tree)
    generate_and_save_graph(
        array, 10, "Create tree", Binary_Search_Tree, "b"
        )
    generate_and_save_graph(array, 10, "Search elements", tree.search, "y")
    generate_and_save_graph(array, 10, "Delete elements", tree.delete, "g")
