from graphing import generate_and_save_graph, test_time
from reader import prepare_text, prepare_words
import n
import kr
import kmp


def find_multiple(words, text, algorithm):
    for word in words:
        algorithm.find(word, text)


if __name__ == "__main__":

    text = prepare_text("pan-tadeusz-unix.txt")

    times_1 = []
    for size in range(1, 11):
        words = prepare_words("pan-tadeusz-unix.txt", 100 * size)
        times_1.append(test_time(find_multiple, words, text, n))
        print(f"finished {size} n")

    times_2 = []
    for size in range(1, 11):
        words = prepare_words("pan-tadeusz-unix.txt", 100 * size)
        times_2.append(test_time(find_multiple, words, text, kr))
        print(f"finished {size} kr")

    times_3 = []
    for size in range(1, 11):
        words = prepare_words("pan-tadeusz-unix.txt", 100 * size)
        times_3.append(test_time(find_multiple, words, text, kmp))
        print(f"finished {size} kmp")

    generate_and_save_graph(
        "Find",
        "time searching depending on number of words",
        times_1,
        times_2,
        times_3
    )
