from dijkstra import dijkstra


def test_1():
    graph = [
        [1, 2, 1, 0],
        [1, 2, 3, 1],
        [2, 2, 1, 1],
        [0, 2, 1, 5]
    ]
    results = dijkstra(graph, (0, 3), (3, 0))
    assert set(results) == {
        (0, 3),
        (1, 3),
        (2, 3),
        (2, 2),
        (3, 2),
        (3, 1),
        (3, 0)
    }


def test_2():
    graph = [
        [0, 8, 8, 0],
        [1, 8, 8, 1],
        [2, 2, 1, 2]
    ]
    results = dijkstra(graph, (0, 0), (0, 3))
    assert set(results) == {
        (0, 0),
        (1, 0),
        (2, 0),
        (2, 1),
        (2, 2),
        (2, 3),
        (1, 3),
        (0, 3)
    }


def test_multiple_paths():
    graph = [
        [1, 1, 0],
        [1, 8, 1],
        [0, 1, 1]
    ]
    results = dijkstra(graph, (0, 2), (2, 0))
    assert (set(results) == {
        (0, 2), (0, 1), (0, 0),
        (1, 0), (2, 0)
    }) or (set(results) == {
        (0, 2), (1, 2), (2, 2),
        (2, 1), (2, 0)
    })


def test_one_point():
    graph = [
        [1, 2, 1, 0],
        [1, 2, 3, 1],
        [2, 2, 1, 1],
        [0, 2, 1, 5]
    ]
    results = dijkstra(graph, (2, 3), (2, 3))
    assert set(results) == {
        (2, 3)
    }
