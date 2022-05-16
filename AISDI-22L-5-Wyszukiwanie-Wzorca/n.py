def find (string, text):
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
        if text[i:(i + len(string))] == string:
            results.append(i)
    return results
