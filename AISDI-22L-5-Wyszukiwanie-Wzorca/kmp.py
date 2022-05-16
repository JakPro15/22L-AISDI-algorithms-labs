def find (string, text):
    """
    Knuth-Morris-Pratt Algorithm
    Parameters:
    string (str): szukany napis
    text (str): przeszukiwany tekst
    Returns:
    (list): lista pozycji w 'text' (w kolejności rosnącej), od
    których zaczyna się 'string'
    """
