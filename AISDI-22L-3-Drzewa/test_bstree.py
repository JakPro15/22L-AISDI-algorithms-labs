from bstree import BinarySearchTree


def test_create_1():
    tree = BinarySearchTree(5)
    assert tree.value == 5


def test_create_none():
    tree_none = BinarySearchTree()
    assert tree_none.value is None


def test_insert_node_left():
    tree = BinarySearchTree(2)
    tree.insert(1)
    assert tree.left_tree.value == 1
    assert tree.right_tree is None


def test_insert_node_right():
    tree = BinarySearchTree(2)
    tree.insert(3)
    assert tree.right_tree.value == 3
    assert tree.left_tree is None


def test_insert_node_advanced_1():
    tree = BinarySearchTree(2)
    tree.insert(4)
    tree.insert(3)
    assert tree.right_tree.left_tree.value == 3


def test_insert_node_advanced_2():
    tree = BinarySearchTree(2)
    tree.insert(4)
    tree.insert(3)
    tree.insert(5)
    assert tree.right_tree.left_tree.value == 3
    assert tree.right_tree.right_tree.value == 5


def test_give_min_1():
    tree = BinarySearchTree(2)
    tree.insert(4)
    tree.insert(3)
    assert tree.give_min() == 2


def test_give_min_2():
    tree = BinarySearchTree(3)
    tree.insert(4)
    tree.insert(3)
    tree.insert(1)
    tree.insert(2)
    assert tree.give_min() == 1


def test_give_max_1():
    tree = BinarySearchTree(2)
    tree.insert(4)
    tree.insert(3)
    assert tree.give_max() == 4


def test_give_max_2():
    tree = BinarySearchTree(3)
    tree.insert(4)
    tree.insert(3)
    tree.insert(5)
    tree.insert(2)
    assert tree.give_max() == 5


def test_delete_node_1():
    tree = BinarySearchTree(2)
    tree.insert(4)
    tree.insert(3)
    tree.delete(3)
    assert tree.right_tree.left_tree is None


def test_delete_node_2():
    tree = BinarySearchTree(2)
    tree.insert(4)
    tree.insert(3)
    tree.insert(5)
    assert tree.right_tree.left_tree.value == 3
    assert tree.right_tree.right_tree.value == 5
