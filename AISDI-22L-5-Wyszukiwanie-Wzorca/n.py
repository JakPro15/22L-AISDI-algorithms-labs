def find (string, text):
    """
    N Algorithm
    Parameters:
    string (str): szukany napis
    text (str): przeszukiwany tekst
    Returns:
    (list): lista pozycji w 'text' (w kolejności rosnącej), od
    których zaczyna się 'string'
    """
    results = []
    for i in range(len(text) - len(string) + 1):
        if i == 2218:
            i = 2218
        tested = text[i:(i + len(string))]
        if tested == string:
            results.append(i)
    return results
