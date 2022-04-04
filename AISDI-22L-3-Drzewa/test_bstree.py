from bstree import BinarySearchTree


def test_create_1():
    tree_1 = BinarySearchTree(5)
    assert tree_1.value == 5


def test_create_none():
    tree_none = BinarySearchTree()
    assert tree_none.value is None


def test_insert_node_left():
    tree_1 = BinarySearchTree(2)
    tree_1.insert(1)
    assert tree_1.left_tree.value == 1
