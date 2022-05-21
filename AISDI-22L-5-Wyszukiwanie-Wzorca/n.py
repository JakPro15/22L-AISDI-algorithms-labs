def compare(string, text, begin):
    for i in range(len(string)):
        if text[begin + i] != string[i]:
            return False
    return True


def find(string, text):
    """
    Naive Algorithm
    Parameters:
    string (str): szukany napis
    text (str): przeszukiwany tekst
    Returns:
    (list): lista pozycji w 'text' (w kolejności rosnącej), od
    których zaczyna się 'string'
    """
    results = []
    for i in range(len(text) - len(string) + 1):
        if compare(string, text, i):
            results.append(i)
    return results
