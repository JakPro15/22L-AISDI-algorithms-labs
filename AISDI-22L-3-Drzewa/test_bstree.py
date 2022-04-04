from bstree import Binary_Search_Tree_Node


def test_create_1():
    tree = Binary_Search_Tree_Node(5)
    assert tree.value == 5


def test_create_none():
    tree_none = Binary_Search_Tree_Node()
    assert tree_none.value is None


def test_insert_node_left():
    tree = Binary_Search_Tree_Node(2)
    tree.insert(1)
    assert tree.left_tree.value == 1
    assert tree.right_tree is None


def test_insert_node_right():
    tree = Binary_Search_Tree_Node(2)
    tree.insert(3)
    assert tree.right_tree.value == 3
    assert tree.left_tree is None


def test_insert_node_advanced_1():
    tree = Binary_Search_Tree_Node(2)
    tree.insert(4)
    tree.insert(3)
    assert tree.right_tree.left_tree.value == 3


def test_insert_node_advanced_2():
    tree = Binary_Search_Tree_Node(2)
    tree.insert(4)
    tree.insert(3)
    tree.insert(5)
    assert tree.right_tree.left_tree.value == 3
    assert tree.right_tree.right_tree.value == 5


def test_give_min_1():
    tree = Binary_Search_Tree_Node(2)
    tree.insert(4)
    tree.insert(3)
    assert tree.give_min() == 2


def test_give_min_2():
    tree = Binary_Search_Tree_Node(3)
    tree.insert(4)
    tree.insert(3)
    tree.insert(1)
    tree.insert(2)
    assert tree.give_min() == 1


def test_give_max_1():
    tree = Binary_Search_Tree_Node(2)
    tree.insert(4)
    tree.insert(3)
    assert tree.give_max() == 4


def test_give_max_2():
    tree = Binary_Search_Tree_Node(3)
    tree.insert(4)
    tree.insert(3)
    tree.insert(5)
    tree.insert(2)
    assert tree.give_max() == 5


def test_delete_node_1():
    tree = Binary_Search_Tree_Node(2)
    tree.insert(4)
    tree.insert(3)
    tree = tree.delete(3)
    assert tree.right_tree.left_tree is None


def test_delete_node_2():
    tree = Binary_Search_Tree_Node(2)
    tree.insert(4)
    tree.insert(3)
    tree.insert(5)
    tree = tree.delete(3)
    assert tree.right_tree.left_tree is None
    assert tree.right_tree.right_tree.value == 5


def test_delete_node_3():
    tree = Binary_Search_Tree_Node(2)
    tree.insert(4)
    tree.insert(3)
    tree.insert(5)
    tree = tree.delete(2)
    assert tree.value == 4
    assert tree.left_tree.value == 3
    assert tree.right_tree.value == 5


def test_delete_node_4():
    tree = Binary_Search_Tree_Node(2)
    tree.insert(4)
    tree.insert(3)
    tree.insert(5)
    tree = tree.delete(4)
    assert tree.value == 2
    assert tree.right_tree.value == 5
    assert tree.right_tree.left_tree.value == 3


def test_delete_node_5():
    tree = Binary_Search_Tree_Node(2)
    tree.insert(1)
    tree.insert(4)
    tree.insert(3)
    tree.insert(5)
    tree = tree.delete(2)
    assert tree.value == 3
    assert tree.right_tree.value == 4
    assert tree.right_tree.right_tree.value == 5
    assert tree.left_tree.value == 1
