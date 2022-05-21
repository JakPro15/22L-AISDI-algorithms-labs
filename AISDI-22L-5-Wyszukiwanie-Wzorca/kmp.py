def find(string, text):
    if string == "":
        return list(range(len(text)))

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
                j = match_table[j - 1]
        elif i < len(text) and string[j] != text[i]:
            if j:
                j = match_table[j - 1]
            else:
                i += 1
    return positions


def compute_match_table_array(string):

    match_table = [0] * len(string)
    suffix_len = 0
    i = 1

    while i < len(string):
        if string[i] == string[suffix_len]:
            suffix_len += 1
            match_table[i] = suffix_len
            i += 1
        else:
            if suffix_len != 0:
                suffix_len = match_table[suffix_len - 1]
            else:
                match_table[i] = 0
                i += 1
    return match_table
