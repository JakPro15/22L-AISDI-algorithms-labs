from graphing import generate_and_save_graph, test_time
from random import randint
from bstree import Binary_Search_Tree
from avl_tree import AVL_Tree


if __name__ == "__main__":
    array = [randint(1, 30000) for x in range(0, 10000)]
    times_create_bst = []
    for size in range(1, 11):
        total_time = test_time(Binary_Search_Tree, array[:size * 1000])
        times_create_bst.append(total_time)
    times_search_bst = []
    for size in range(1, 11):
        tree = Binary_Search_Tree(array)
        total_time = test_time(tree.search, array[:size * 1000])
        times_search_bst.append(total_time)
    times_delete_bst = []
    for size in range(1, 11):
        tree = Binary_Search_Tree(array)
        total_time = test_time(tree.delete, array[:size * 1000])
        times_delete_bst.append(total_time)

    times_create_avl = []
    for size in range(1, 11):
        total_time = test_time(AVL_Tree, array[:size * 1000])
        times_create_avl.append(total_time)
    times_search_avl = []
    for size in range(1, 11):
        tree = AVL_Tree(array)
        total_time = test_time(tree.search, array[:size * 1000])
        times_search_avl.append(total_time)
    times_delete_avl = []
    for size in range(1, 11):
        tree = AVL_Tree(array)
        total_time = test_time(tree.delete, array[:size * 1000])
        times_delete_avl.append(total_time)

    generate_and_save_graph(
        "Create_tree",
        "time of creation depending on the list's length",
        times_create_bst, times_create_avl
    )
    generate_and_save_graph(
        "Search_elements",
        "time of search depending on number of elements searched",
        times_search_bst, times_search_avl
    )
    generate_and_save_graph(
        "Delete_elements",
        "time of deletion depending on number of elements deleted",
        times_delete_bst, times_delete_avl
    )
