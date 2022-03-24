def bubble_sort(array):
    for i in range(0, len(array) - 1):
        swap = False
        for j in range(i, len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swap = True
        if not swap:
            break
    return array


def selection_sort(array):
    array_copy = array
    sorted_array = []
    while array_copy:
        sorted_array.append(min(array_copy))
        array_copy.remove(min(array_copy))
    return sorted_array


def merge_sort(array):
    if len(array) <= 1:
        return array
    midpoint = len(array) // 2
    left_array = array[:midpoint]
    right_array = array[midpoint:]
    left_array = merge_sort(left_array)
    right_array = merge_sort(right_array)
    return merge(left_array, right_array)


def merge(array_1, array_2):
    final_list = []
    while array_1 and array_2:
        if array_1[0] <= array_2[0]:
            final_list.append(array_1[0])
            array_1.remove(array_1[0])
        else:
            final_list.append(array_2[0])
            array_2.remove(array_2[0])
    while array_1:
        final_list.append(array_1[0])
        array_1.remove(array_1[0])
    while array_2:
        final_list.append(array_2[0])
        array_2.remove(array_2[0])
    return final_list


def quick_sort(array):
    return quick_sort_part(array, 0, len(array) - 1)


def quick_sort_part(array, begin, end):
    if len(array) <= 1:
        return array
    if begin < end:
        ptn = partition(array, begin, end)
        quick_sort_part(array, begin, ptn - 1)
        quick_sort_part(array, ptn + 1, end)


def partition(array, begin, end):
    pivot = array[(begin + end) // 2]
    i = begin - 1
    for j in range(begin, end):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[end] = array[end], array[i + 1]
    return i + 1