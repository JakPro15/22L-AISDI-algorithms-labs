from graphing import generate_and_save_graph, test_time
from random import randint
from bstree import Binary_Search_Tree
from copy import copy


if __name__ == "__main__":
    array = [randint(1, 30000) for x in range(0, 10000)]
    tree = Binary_Search_Tree(array)
    times_create = []
    for size in range(1, 11):
        total_time = test_time(Binary_Search_Tree, array[:size * 1000])
        times_create.append(total_time)
    times_search = []
    for size in range(1, 11):
        tree = copy(tree)
        total_time = test_time(tree.search, array[:size * 1000])
        times_search.append(total_time)
    times_delete = []
    for size in range(1, 11):
        tree = copy(tree)
        total_time = test_time(tree.delete, array[:size * 1000])
        times_delete.append(total_time)
    generate_and_save_graph(
        "Create_tree_-_BST",
        "time of creation depending on the list length", "b", times_create
        )
    generate_and_save_graph(
        "Search_elements_-_BST",
        "time of search depending on number of elements", "y", times_search
        )
    generate_and_save_graph(
        "Delete_elements_-_BST",
        "time of deletion depending on number of elements", "g", times_delete
        )
