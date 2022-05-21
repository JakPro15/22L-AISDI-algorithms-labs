import n
import kr
import kmp
from random import randint


def test_find(algorithm_name, function, string, text):
    print(f'Looking for "{string}" using {algorithm_name}')
    indexes = function(string, text)
    print(text)
    stri = ""
    for i in range(len(text)):
        if i in indexes:
            stri += "^"
        else:
            stri += " "
    print(stri)


def generate(length):
    result = ""
    for _ in range(length):
        if(randint(0, 1) == 1):
            result += "A"
        else:
            result += "B"
    return result


def comparison_test(string_len, text_len):
    string = generate(string_len)
    text = generate(text_len)
    n_res = n.find(string, text)
    kr_res = kr.find(string, text)
    kmp_res = kmp.find(string, text)
    assert n_res == kr_res
    assert n_res == kmp_res
    print(f"Looking for {string}:")
    print(text)
    stri = ""
    for i in range(len(text)):
        if i in n_res:
            stri += "^"
        else:
            stri += " "
    print(stri)
    print("All algorithms gave the same results.")


if __name__ == "__main__":
    print("Looking for an empty string")
    test_find("Naive Algorithm", n.find, "", "asdgrweghtestgebtestestgb")
    test_find("Rabin-Karp Algorithm", kr.find, "", "asdgrweghtestgebtestestgb")
    test_find("Knuth-Morris-Pratt Algorithm", kmp.find, "", "asdgrweghtestgebtestestgb")
    print("-----------------------------------")
    print("Looking in an empty string")
    test_find("Naive Algorithm", n.find, "test", "")
    test_find("Rabin-Karp Algorithm", kr.find, "test", "")
    test_find("Knuth-Morris-Pratt Algorithm", kmp.find, "test", "")
    print("-----------------------------------")
    print("Both strings empty")
    test_find("Naive Algorithm", n.find, "", "")
    test_find("Rabin-Karp Algorithm", kr.find, "", "")
    test_find("Knuth-Morris-Pratt Algorithm", kmp.find, "", "")
    print("-----------------------------------")
    print("Both strings equal")
    test_find("Naive Algorithm", n.find, "Test", "Test")
    test_find("Rabin-Karp Algorithm", kr.find, "Test", "Test")
    test_find("Knuth-Morris-Pratt Algorithm", kmp.find, "Test", "Test")
    print("-----------------------------------")
    print("String longer than text")
    test_find("Naive Algorithm", n.find, "Tester", "Test")
    test_find("Rabin-Karp Algorithm", kr.find, "Tester", "Test")
    test_find("Knuth-Morris-Pratt Algorithm", kmp.find, "Tester", "Test")
    print("-----------------------------------")
    print("String not in text")
    test_find("Naive Algorithm", n.find, "Tester", "Testadostorostomosto")
    test_find("Rabin-Karp Algorithm", kr.find, "Tester", "Testadostorostomosto")
    test_find("Knuth-Morris-Pratt Algorithm", kmp.find, "Tester", "Testadostorostomosto")
    print("-----------------------------------")
    print("Naive Algorithm testing")
    test_find("Naive Algorithm", n.find, "ABCDDCAB", "DCBABCDDCABCDDCABEABCDDCA")
    test_find("Naive Algorithm", n.find, "a", "Ja i mój kot Makoś")
    test_find("Naive Algorithm", n.find, "ESS", "ESSASSESSESSSessESSS")
    test_find("Naive Algorithm", n.find, "arol", "Król Karol kupił królowej Karolinie korale koloru koralowego")
    print("-----------------------------------")
    print("Comparison testing")
    comparison_test(4, 9)
    comparison_test(2, 14)
    comparison_test(7, 8)
    comparison_test(1, 7)
    comparison_test(1, 7)
