import gc
import time
from matplotlib import pyplot as plt


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


def generate_and_save_graph(name, description, color, times):
    keys = [i * 1000 for i in range(1, 11)]
    title = ""
    for letter in name:
        if letter != "_":
            title += letter
        else:
            title += " "
    plt.plot(
        keys, times, 'o-', label=f"{title}", markersize=3, color=color
    )
    plt.legend()
    plt.title(f"{title} - {description}")
    plt.xlabel("Number of elements")
    plt.ylabel("Time of process in seconds")
    plt.xticks(keys, [str(element) for element in keys])
    plt.savefig(f"graph_{name.lower()}.png")
    plt.clf()
