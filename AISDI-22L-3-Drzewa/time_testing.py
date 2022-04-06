from time_functions import test_time
from bstree import Binary_Search_Tree
from random import randint


array = [randint(1, 30000) for x in range(0, 10000)]
print(test_time(Binary_Search_Tree, array))
tree = Binary_Search_Tree(array)
print(test_time(tree.search, array[:2000]))
print(test_time(tree.delete, array[:2000]))
