def prepare_text(text_file):
    with open(text_file, "r") as file:
        text = file.read()
    return text


polish_letters_list = ['ć', 'ń', 'ó', 'ś', 'ź', 'ż', 'ą', 'ę', 'ł',
                       'Ć', 'Ń', 'Ó', 'Ś', 'Ź', 'Ż', 'Ł']


def prepare_words(text_file, word_limit):
    with open(text_file, "r") as file:
        text = file.read()
        text_split_by_lines = text.splitlines()
        text_array = []
        for line in text_split_by_lines:
            line = line.split(" ")
            text_array.append(line)
        new_text_array = []
        for line in text_array:
            for word in line:
                if len(new_text_array) == word_limit:
                    break
                new_word = ""
                for letter in word:
                    if (
                        (64 < ord(letter) < 91) or
                        (96 < ord(letter) < 123) or
                        (letter in polish_letters_list)
                            ):
                        new_word += letter
                if new_word:
                    new_text_array.append(new_word)
    return new_text_array
