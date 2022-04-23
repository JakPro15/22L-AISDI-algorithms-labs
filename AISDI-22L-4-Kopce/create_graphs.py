from graphing import generate_and_save_graph, test_time
from random import randint
from heaps import insert_list, extract_n

if __name__ == "__main__":
    array = [randint(1, 300000) for _ in range(0, 100000)]
    times_create_2 = []
    for size in range(1, 11):
        heap = [-1]
        total_time = test_time(insert_list, heap, array[:size * 10000], 2)
        times_create_2.append(total_time)
        print(f"AJAJAJAJA{size} time:{total_time}")
    times_extract_2 = []
    for size in range(1, 11):
        heap = [-1]
        insert_list(heap, array, 2)
        total_time = test_time(extract_n, heap, size * 10000, 2)
        times_extract_2.append(total_time)
        print(f"AXAXAXAXAXA{size} time:{total_time}")
    times_create_3 = []
    for size in range(1, 11):
        heap = [-1]
        total_time = test_time(insert_list, heap, array[:size * 10000], 3)
        times_create_3.append(total_time)
        print(f"tripleb{size} time:{total_time}")
    times_extract_3 = []
    for size in range(1, 11):
        heap = [-1]
        insert_list(heap, array, 3)
        total_time = test_time(extract_n, heap, size * 10000, 3)
        times_extract_3.append(total_time)
        print(f"turipluh{size} time:{total_time}")
    times_create_4 = []
    for size in range(1, 11):
        heap = [-1]
        total_time = test_time(insert_list, heap, array[:size * 10000], 4)
        times_create_4.append(total_time)
        print(f"quadurupuluh{size} time:{total_time}")
    times_extract_4 = []
    for size in range(1, 11):
        heap = [-1]
        insert_list(heap, array, 4)
        total_time = test_time(extract_n, heap, size * 10000, 4)
        times_extract_4.append(total_time)
        print(f"420 {size} time:{total_time}")

    generate_and_save_graph(
        "Create_heap",
        "time of creation depending on list's length",
        times_create_2,
        times_create_3,
        times_create_4
    )

    generate_and_save_graph(
        "Extract_root",
        "time of extraction of largest elements depending on their amount",
        times_extract_2,
        times_extract_3,
        times_extract_4
    )
