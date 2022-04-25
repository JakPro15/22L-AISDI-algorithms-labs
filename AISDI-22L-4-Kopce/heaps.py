def insert(heap, value, dimension):
    heap.append(value)
    element = len(heap) - 1
    parent = max((element - 2) // dimension + 1, 1)
    while (heap[parent] < value):
        heap[parent], heap[element] = heap[element], heap[parent]
        element = parent
        parent = max((element - 2) // dimension + 1, 1)


def extract(heap, dimension):
    if len(heap) > 1:
        if len(heap) != 2:
            element = len(heap) - 1
            heap[1], heap[element] = heap[element], heap[1]
            heap.pop()

            parent = 1
            while True:
                first_child = dimension * (parent - 1) + 2
                range_end = min(len(heap), first_child + dimension)

                biggest = parent
                for child in range(first_child, range_end):
                    if heap[child] > heap[biggest]:
                        biggest = child
                
                if biggest == parent:
                    break
                else:
                    heap[parent], heap[biggest] = heap[biggest], heap[parent]
                    parent = biggest


def insert_list(heap, array, dimension):
    for element in array:
        insert(heap, element, dimension)


def extract_n(heap, amount, dimension):
    for _ in range(amount):
        extract(heap, dimension)
