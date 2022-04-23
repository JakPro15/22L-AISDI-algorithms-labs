from numpy import true_divide


def insert(heap, value, dimension):
    if value not in heap:
        heap.append(value)
        parent = max(heap.index(value) // dimension, 1)
        element = heap.index(value)
        while (heap[parent] < value):
            heap[parent], heap[element] = heap[element], heap[parent]
            parent = max(heap.index(value) // dimension, 1)
            element = heap.index(value)
    return heap


def extract(heap, dimension):
    element = len(heap) - 1
    heap[1], heap[element] = heap[element], heap[1]
    all_ok = True
    for k in range(dimension):
        if heap[1] < heap[1 + k]:
            all_ok = False
