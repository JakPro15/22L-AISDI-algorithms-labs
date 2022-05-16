def find(string, text):

    positions = []
    i = 0
    j = 0

    match_table = compute_match_table_array(string)

    while i < len(text):
        if string[j] == text[i]:
            i += 1
            j += 1
            if j == len(string):
                positions.append(i - j)
                j = match_table[j]
        else:
            j = match_table[j]
            if j < 0:
                i += 1
                j += 1
    return positions


def compute_match_table_array(string):

    position = 1
    string_index = 0

    match_table = [-1] * (len(string) + 1)
    match_table[0] = -1

    while position < len(string):
        if string[position] == string[string_index]:
            match_table[position] = match_table[string_index]
        else:
            match_table[position] == string_index
            while (string_index >= 0 and
                    string[position] != string[string_index]):
                string_index = match_table[string_index]
        position += 1
        string_index += 1

    match_table[position] = string_index
    return match_table
