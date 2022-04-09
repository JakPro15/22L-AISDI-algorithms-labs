from avl_tree import AVL_Tree
from random import randint


if __name__ == "__main__":
    tree = AVL_Tree([randint(0, 99) for _ in range(20)])
    tree.print_tree()
