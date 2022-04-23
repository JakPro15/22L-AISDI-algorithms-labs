def insert(heap, value, dimension):
    if value not in heap:
        heap.append(value)
        parent = max(heap.index(value) // dimension, 1)
        element = len(heap) - 1
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
            if not all_ok:
                biggest_child = heap.index(max(heap[2:1 + dimension]))
                heap[1], heap[biggest_child] = heap[biggest_child], heap[1]
    else:
        if heap[1] != max(heap[1:]):
            biggest_child = heap.index(max(heap[1:]))
            heap[1], heap[biggest_child] = heap[biggest_child], heap[1]
