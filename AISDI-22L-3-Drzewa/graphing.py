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


def generate_and_save_graph(name, description, times_bst, times_avl):
    keys = [i * 1000 for i in range(1, 11)]
    title = ""
    for letter in name:
        if letter != "_":
            title += letter
        else:
            title += " "
    plt.plot(
        keys, times_bst, 'o-', label="BST", markersize=3, color='b'
    )
    plt.plot(
        keys, times_avl, 'o-', label="AVL", markersize=3, color='y'
    )
    plt.legend()
    plt.title(f"{title} - {description}")
    plt.xlabel("Number of elements")
    plt.ylabel("Time in seconds")
    plt.xticks(keys, [str(element) for element in keys])
    plt.savefig(f"graph_{name.lower()}.png")
    plt.clf()
