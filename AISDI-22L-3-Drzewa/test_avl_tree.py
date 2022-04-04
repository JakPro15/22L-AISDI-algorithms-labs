from avl_tree import AVL_Tree


def test_1():
    values = list(range(1000))
    tree = AVL_Tree(values)

    def go_down_the_tree(node, max, min):
        assert node.balance_factor in {-1, 0, 1}
        if max:
            assert node.value < max
        if min:
            assert node.value > min
        if node.left_tree:
            go_down_the_tree(node.left_tree, min=min, max=node.value)
        if node.right_tree:
            go_down_the_tree(node.left_tree, min=node.value, max=max)
    
    go_down_the_tree(tree.root, None, None)
