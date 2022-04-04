from bstree import Binary_Search_Tree_Node, Binary_Search_Tree


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


def test_delete_node_1():
    tree = Binary_Search_Tree([2, 4, 3])
    tree.delete(3)
    assert tree.root.right_tree.left_tree is None


def test_delete_node_2():
    tree = Binary_Search_Tree([2, 4, 3, 5])
    tree.delete(3)
    assert tree.root.right_tree.left_tree is None
    assert tree.root.right_tree.right_tree.value == 5


def test_delete_node_3():
    tree = Binary_Search_Tree([2, 4, 3, 5])
    tree.delete(2)
    assert tree.root.value == 4
    assert tree.root.left_tree.value == 3
    assert tree.root.right_tree.value == 5


def test_delete_node_4():
    tree = Binary_Search_Tree([2, 4, 3, 5])
    tree.delete(4)
    assert tree.root.value == 2
    assert tree.root.right_tree.value == 5
    assert tree.root.right_tree.left_tree.value == 3


def test_delete_node_5():
    tree = Binary_Search_Tree([2, 1, 4, 3, 5])
    tree.delete(2)
    assert tree.root.value == 3
    assert tree.root.right_tree.value == 4
    assert tree.root.right_tree.right_tree.value == 5
    assert tree.root.left_tree.value == 1
