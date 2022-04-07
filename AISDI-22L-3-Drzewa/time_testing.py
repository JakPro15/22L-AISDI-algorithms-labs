from time_functions import test_time
from bstree import Binary_Search_Tree
from random import randint


def random_test():
    array = [randint(1, 30000) for x in range(0, 10000)]
    tree = Binary_Search_Tree(array)
    print(f"Creation of the tree: {test_time(Binary_Search_Tree, array)}")
    print(f"Searching of all elements: {test_time(tree.search, array)}")
    print(f"Deletion of all elements: {test_time(tree.delete, array)}")


if __name__ == "__main__":
    random_test()
