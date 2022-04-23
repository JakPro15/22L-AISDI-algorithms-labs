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
    if len(heap) > 1:
        if len(heap) != 2:
            element = len(heap) - 1
            heap[1], heap[element] = heap[element], heap[1]
            heap.pop()
            all_ok = False
            while not all_ok:
                n = 1
                all_ok = True
                if len(heap) >= dimension * n + 2:
                    for k in range(dimension):
                        if heap[n] < heap[dimension * (n - 1) + 2 + k]:
                            all_ok = False
                            break
                    if not all_ok:
                        b_child = biggest_child_index(heap, n, dimension)
                        heap[n], heap[b_child] = heap[b_child], heap[n]
                        n = b_child
                else:
                    largest = n
                    for k in range(n + 1, len(heap)):
                        if heap[largest] < heap[k]:
                            largest = k
                    heap[n], heap[largest] = heap[largest], heap[n]


def biggest_child_index(heap, n, dimension):
    biggest_child = dimension * (n - 1) + 2
    for k in range(biggest_child, biggest_child + dimension):
        if heap[k] > heap[biggest_child]:
            biggest_child = k
    return biggest_child


def insert_list(heap, array, dimension):
    for element in array:
        insert(heap, element, dimension)


def extract_n(heap, amount, dimension):
    for _ in range(amount):
        extract(heap, dimension)
