import gc
import time
from matplotlib import pyplot as plt


def test_time(process, *args):
    gc_old = gc.isenabled()
    gc.disable()

    start_time = time.process_time()
    process(*args)
    end_time = time.process_time()

    if gc_old:
        gc.enable()

    return end_time - start_time


def generate_and_save_graph(name, description, times_2, times_3, times_4):
    keys = [i * 100 for i in range(1, 11)]
    title = ""
    for letter in name:
        if letter != "_":
            title += letter
        else:
            title += " "
    plt.plot(
        keys, times_2, 'o-', label="n", markersize=3, color='b'
    )
    plt.plot(
        keys, times_3, 'o-', label="kr", markersize=3, color='y'
    )
    plt.plot(
        keys, times_4, 'o-', label="kmp", markersize=3, color='g'
    )
    plt.legend()
    plt.title(f"{title} - {description}")
    plt.xlabel("Number of words")
    plt.ylabel("Time in seconds")
    plt.xticks(keys, [str(element) for element in keys])
    plt.savefig(f"graph_{name.lower()}.png")
    plt.clf()
