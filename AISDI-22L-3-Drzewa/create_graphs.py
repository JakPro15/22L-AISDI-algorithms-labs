from graphing import save_all_graphs
from random import randint
from bstree import Binary_Search_Tree


if __name__ == "__main__":
    array = [randint(1, 30000) for x in range(0, 10000)]
    tree = Binary_Search_Tree(array)
    save_all_graphs(array, tree)
