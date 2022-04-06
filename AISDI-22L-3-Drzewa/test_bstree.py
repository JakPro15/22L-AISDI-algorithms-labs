from bstree import Binary_Search_Tree_Node, Binary_Search_Tree


def test_create_node_1():
    tree = Binary_Search_Tree_Node(5)
    assert tree.value == 5


def test_create_node_none():
    tree_none = Binary_Search_Tree_Node()
    assert tree_none.value is None


def test_insert_node_left():
    tree = Binary_Search_Tree([2])
    tree.insert(1)
    assert tree.root.left_tree.value == 1
    assert tree.root.right_tree is None


def test_insert_node_right():
    tree = Binary_Search_Tree([2])
    tree.insert(3)
    assert tree.root.right_tree.value == 3
    assert tree.root.left_tree is None


def test_insert_node_advanced_1():
    tree = Binary_Search_Tree([2])
    tree.insert(4)
    tree.insert(3)
    assert tree.root.right_tree.left_tree.value == 3


def test_insert_node_advanced_2():
    tree = Binary_Search_Tree([2])
    tree.insert(4)
    tree.insert(3)
    tree.insert(5)
    assert tree.root.right_tree.left_tree.value == 3
    assert tree.root.right_tree.right_tree.value == 5


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


def test_search_tree_1():
    tree = Binary_Search_Tree([2, 1, 4, 3, 5])
    assert tree.search(1).value == 1
    assert tree.search(3).value == 3
    assert tree.search(5).value == 5
    assert tree.search(7) is None


def test_search_tree_2():
    tree = Binary_Search_Tree([2, 1, 4, 3])
    assert tree.search(1).value == 1
    assert tree.search(3).value == 3
    assert tree.search(5) is None
    assert tree.search(7) is None


def test_search_tree_3():
    tree = Binary_Search_Tree([2, 1, 4])
    assert tree.search(1).value == 1
    assert tree.search(3) is None
    assert tree.search(5) is None
    assert tree.search(7) is None
