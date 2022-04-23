def insert(heap, value, dimension):
    if value not in heap:
        heap.append(value)
        element = len(heap) - 1
        parent = max(element // dimension, 1)
        while (heap[parent] < value):
            heap[parent], heap[element] = heap[element], heap[parent]
            element = parent
            parent = max(element // dimension, 1)


def extract(heap, dimension):
    element = len(heap) - 1
    heap[1], heap[element] = heap[element], heap[1]
    heap.pop()
    all_ok = False
    if len(heap) >= dimension + 2:
        while not all_ok:
            all_ok = True
            for k in range(dimension):
                if heap[1] < heap[2 + k]:
                    all_ok = False
                    break
            if not all_ok:
                biggest_child = biggest_child_index(heap, dimension)
                heap[1], heap[biggest_child] = heap[biggest_child], heap[1]
    else:
        if len(heap) != 1:
            if heap[1] != max(heap):
                biggest_child = heap.index(max(heap))
                heap[1], heap[biggest_child] = heap[biggest_child], heap[1]


def biggest_child_index(heap, dimension):
    biggest_child = 2
    for k in range(2, 2 + dimension):
        if heap[k] > heap[biggest_child]:
            biggest_child = k
    return biggest_child
