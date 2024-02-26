from avl_tree import AVL_Tree
from random import randint, gauss


def get_subtree_height(node):
    if node.left_child and node.right_child:
        tree_height = max(
            get_subtree_height(node.left_child),
            get_subtree_height(node.right_child)
        )
    elif node.left_child:
        tree_height = get_subtree_height(node.left_child)
    elif node.right_child:
        tree_height = get_subtree_height(node.right_child)
    else:
        tree_height = 0
    return tree_height + 1


def checker_avl(node, max, min):
    if node.left_child:
        left_height = get_subtree_height(node.left_child)
    else:
        left_height = 0

    if node.right_child:
        right_height = get_subtree_height(node.right_child)
    else:
        right_height = 0

    assert node.balance_factor == right_height - left_height
    if max:
        assert node.value < max
    if min:
        assert node.value > min
    if node.left_child:
        checker_avl(node.left_child, min=min, max=node.value)
    if node.right_child:
        checker_avl(node.right_child, min=node.value, max=max)


def test_basic_avl_tree_1():
    tree = AVL_Tree([1])
    checker_avl(tree.root, None, None)
    assert tree.root.parent is tree
    assert tree.root.value == 1
    assert tree.root.left_child is None
    assert tree.root.right_child is None
    assert tree.root.balance_factor == 0


def test_basic_avl_tree_2():
    tree = AVL_Tree([1, 0])
    checker_avl(tree.root, None, None)
    assert tree.root.parent is tree
    assert tree.root.value == 1
    assert tree.root.right_child is None
    assert tree.root.balance_factor == -1

    assert tree.root.left_child.parent is tree.root
    assert tree.root.left_child.value == 0
    assert tree.root.left_child.left_child is None
    assert tree.root.left_child.right_child is None
    assert tree.root.left_child.balance_factor == 0


def test_basic_avl_tree_3():
    tree = AVL_Tree([1, 0, 2])
    checker_avl(tree.root, None, None)
    assert tree.root.parent is tree
    assert tree.root.value == 1
    assert tree.root.balance_factor == 0

    assert tree.root.left_child.parent is tree.root
    assert tree.root.left_child.value == 0
    assert tree.root.left_child.left_child is None
    assert tree.root.left_child.right_child is None
    assert tree.root.left_child.balance_factor == 0

    assert tree.root.right_child.parent is tree.root
    assert tree.root.right_child.value == 2
    assert tree.root.right_child.left_child is None
    assert tree.root.right_child.right_child is None
    assert tree.root.right_child.balance_factor == 0


def test_basic_avl_tree_right_rotation():
    # Here a right rotation is needed
    tree = AVL_Tree([1, 0, -1])
    checker_avl(tree.root, None, None)
    assert tree.root.parent is tree
    assert tree.root.value == 0
    assert tree.root.balance_factor == 0

    assert tree.root.left_child.parent is tree.root
    assert tree.root.left_child.value == -1
    assert tree.root.left_child.left_child is None
    assert tree.root.left_child.right_child is None
    assert tree.root.left_child.balance_factor == 0

    assert tree.root.right_child.parent is tree.root
    assert tree.root.right_child.value == 1
    assert tree.root.right_child.left_child is None
    assert tree.root.right_child.right_child is None
    assert tree.root.right_child.balance_factor == 0


def test_basic_avl_tree_left_rotation():
    # Here a left rotation is needed
    tree = AVL_Tree([-1, 0, 1])
    checker_avl(tree.root, None, None)
    assert tree.root.parent is tree
    assert tree.root.value == 0
    assert tree.root.balance_factor == 0

    assert tree.root.left_child.parent is tree.root
    assert tree.root.left_child.value == -1
    assert tree.root.left_child.left_child is None
    assert tree.root.left_child.right_child is None
    assert tree.root.left_child.balance_factor == 0

    assert tree.root.right_child.parent is tree.root
    assert tree.root.right_child.value == 1
    assert tree.root.right_child.left_child is None
    assert tree.root.right_child.right_child is None
    assert tree.root.right_child.balance_factor == 0


def test_basic_avl_tree_left_right_rotation():
    # Here a left-right rotation is needed
    tree = AVL_Tree([1, -1, 0])
    checker_avl(tree.root, None, None)
    assert tree.root.parent is tree
    assert tree.root.value == 0
    assert tree.root.balance_factor == 0

    assert tree.root.left_child.parent is tree.root
    assert tree.root.left_child.value == -1
    assert tree.root.left_child.left_child is None
    assert tree.root.left_child.right_child is None
    assert tree.root.left_child.balance_factor == 0

    assert tree.root.right_child.parent is tree.root
    assert tree.root.right_child.value == 1
    assert tree.root.right_child.left_child is None
    assert tree.root.right_child.right_child is None
    assert tree.root.right_child.balance_factor == 0


def test_basic_avl_tree_right_left_rotation():
    # Here a right-left rotation is needed
    tree = AVL_Tree([-1, 1, 0])
    checker_avl(tree.root, None, None)
    assert tree.root.parent is tree
    assert tree.root.value == 0
    assert tree.root.balance_factor == 0

    assert tree.root.left_child.parent is tree.root
    assert tree.root.left_child.value == -1
    assert tree.root.left_child.left_child is None
    assert tree.root.left_child.right_child is None
    assert tree.root.left_child.balance_factor == 0

    assert tree.root.right_child.parent is tree.root
    assert tree.root.right_child.value == 1
    assert tree.root.right_child.left_child is None
    assert tree.root.right_child.right_child is None
    assert tree.root.right_child.balance_factor == 0


def test_sorted_list():
    values = list(range(5))
    tree = AVL_Tree(values)

    checker_avl(tree.root, None, None)
    for value in values:
        assert tree.search([value])[0].value == value
    for value in values:
        tree.delete([value])
        assert len(tree.search([value])) == 0
        if tree.root:
            checker_avl(tree.root, None, None)


def test_random_list():
    values = [randint(0, 1000) for _ in range(1000)]
    tree = AVL_Tree(values)

    checker_avl(tree.root, None, None)
    for value in values:
        assert tree.search([value])[0].value == value
    for value in values:
        tree.delete([value])
        assert len(tree.search([value])) == 0
        if tree.root:
            checker_avl(tree.root, None, None)


def test_gauss_random_list():
    values = [gauss(500, 250) for _ in range(1000)]
    tree = AVL_Tree(values)

    checker_avl(tree.root, None, None)
    for value in values:
        assert tree.search([value])[0].value == value
    for value in values:
        tree.delete([value])
        assert len(tree.search([value])) == 0
        if tree.root:
            checker_avl(tree.root, None, None)
