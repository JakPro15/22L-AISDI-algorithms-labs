def bubble_sort(array):
    new_array = array.copy()
    for i in range(len(new_array) - 1):
        swap = False
        for j in range(len(new_array) - 1 - i):
            if new_array[j] > new_array[j + 1]:
                new_array[j], new_array[j + 1] = new_array[j + 1], new_array[j]
                swap = True
        if not swap:
            break
    return new_array


def selection_sort(array):
    new_array = array.copy()
    for i in range(len(new_array) - 1):
        min_index = new_array[i:].index(min(new_array[i:])) + i
        new_array[i], new_array[min_index] = new_array[min_index], new_array[i]
    return new_array


def merge_sort(array):
    new_array = array.copy()
    if len(new_array) <= 1:
        return new_array
    midpoint = len(new_array) // 2
    left_array = new_array[:midpoint]
    right_array = new_array[midpoint:]
    left_array = merge_sort(left_array)
    right_array = merge_sort(right_array)
    return merge(left_array, right_array)


def merge(array_1, array_2):
    final_list = []
    index_1 = 0
    index_2 = 0
    while index_1 < len(array_1) and index_2 < len(array_2):
        if array_1[index_1] <= array_2[index_2]:
            final_list.append(array_1[index_1])
            index_1 += 1
        else:
            final_list.append(array_2[index_2])
            index_2 += 1
    while index_1 < len(array_1):
        final_list.append(array_1[index_1])
        index_1 += 1
    while index_2 < len(array_2):
        final_list.append(array_2[index_2])
        index_2 += 1
    return final_list


def quick_sort(array):
    new_array = array.copy()
    quick_sort_part(new_array, 0, len(new_array) - 1)
    return new_array


def quick_sort_part(array, begin, end):
    if begin < end:
        partition_point = partition(array, begin, end)
        quick_sort_part(array, begin, partition_point - 1)
        quick_sort_part(array, partition_point + 1, end)


def partition(array, begin, end):
    pivot = array[(begin + end) // 2]
    array[(begin + end) // 2], array[end] = \
        array[end], array[(begin + end) // 2]
    i = begin - 1
    for j in range(begin, end):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[end] = array[end], array[i + 1]
    return i + 1
