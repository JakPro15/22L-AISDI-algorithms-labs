from graphing import generate_and_save_graph, test_time
from random import randint
from reader import prepare_text, prepare_words
import n
import kr
import kmp

if __name__ == "__main__":

    text = prepare_text("pan-tadeusz-unix.txt")

    times_1 = []
    for size in range(1, 11):
        words = prepare_words("pan-tadeusz-unix.txt", 100 * size)

    generate_and_save_graph(
        "Find",
        "time searching depending on number of words",
        times_1,
        times_2,
        times_3
    )
