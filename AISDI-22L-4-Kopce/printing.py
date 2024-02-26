from heaps import insert_list
from sys import argv


def get_max_digits(heap):
    digits_list = [len(str(val)) for val in heap]
    digits = max(digits_list)

    if digits % 2 == 0:
        digits += 1
    return digits


def print_heap(heap, dim: int):
    lines = [[]]
    index = 1
    line_index = 0
    while index < len(heap):
        if line_index == len(lines):
            lines.append([])
        lines[line_index].append(heap[index])
        index += 1
        if len(lines[line_index]) == dim ** line_index:
            line_index += 1

    h = len(lines) - 1
    n = get_max_digits(heap)
    for i, line in enumerate(lines):
        dist = dim ** (h - i) * (n + 1) - n

        if i != 0:
            underscores = ' ' * (dist // 2 + n // 2 + 1)
            for j, val in enumerate(line):
                if j % dim == 0:
                    underscores += '_' * (((dim - 1) * (dist + n) - 1) // 2)
                    underscores += '⊥'
                    underscores += '_' * (((dim - 1) * (dist + n) - 1) // 2)
                elif j % dim == dim - 1 and j != len(line) - 1:
                    underscores += ' ' * (dist + n + 1)
            print(underscores)

            slashes = ' ' * (dist // 2 + n // 2)
            for j, val in enumerate(line):
                if j % dim == 0:
                    slashes += '/'
                elif j % dim == dim - 1:
                    slashes += '\\'
                else:
                    slashes += '|'
                if j != len(line) - 1:
                    slashes += ' ' * (dist + n - 1)
            print(slashes)

        numbers = ' ' * (dist // 2)
        for j, val in enumerate(line):
            numbers += f"{val:^{n}}"
            if j != len(line) - 1:
                numbers += ' ' * dist
        print(numbers)


dim = int(argv[1])
size = int(argv[2])
heap = [None]
insert_list(heap, list(range(size)), dim)
print_heap(heap, dim)
