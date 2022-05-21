BASE = 128  # ASCII characters fit, polish signs don't - I assume they are rare
PRIME_MODULUS = 48247


def compare(string, text, begin):
    for i in range(len(string)):
        if text[begin + i] != string[i]:
            return False
    return True


def hash(string, length, begin=0):
    result = ord(string[begin])
    for i in range(1, length):
        result *= BASE
        result += ord(string[begin + i])
        result %= PRIME_MODULUS
    return result


def rehash(old_hash, old_char, new_char, base_offset):
    result = (
        ((old_hash - (ord(old_char) * base_offset)) * BASE) + ord(new_char)
    ) % PRIME_MODULUS
    return result


def find(string, text):
    """
    Karp-Rabin Algorithm
    Parameters:
    string (str): szukany napis
    text (str): przeszukiwany tekst
    Returns:
    (list): lista pozycji w 'text' (w kolejności rosnącej), od
    których zaczyna się 'string'
    """
    base_offset = (BASE ** (len(string) - 1)) % PRIME_MODULUS

    if string == "":
        return list(range(len(text)))
    if len(text) < len(string):
        return []
    results = []
    string_hash = hash(string, len(string))
    current_hash = hash(text, len(string))

    if string_hash == current_hash:
        if compare(string, text, 0):
            results.append(0)

    for i in range(1, len(text) - len(string) + 1):
        current_hash = rehash(
            current_hash, text[i - 1], text[i + len(string) - 1], base_offset
        )
        if current_hash == string_hash:
            if compare(string, text, i):
                results.append(i)
    return results
