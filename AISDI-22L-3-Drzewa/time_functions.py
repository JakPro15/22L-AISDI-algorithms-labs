import gc
import time


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
