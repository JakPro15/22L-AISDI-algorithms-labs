from bstree import Binary_Search_Tree
from random import randint


if __name__ == "__main__":
    tree = Binary_Search_Tree([randint(0, 99) for _ in range(20)])
    tree.print_tree()
