from avl_tree import AVL_Tree


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


def go_down_the_tree(node, max, min):
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
        go_down_the_tree(node.left_child, min=min, max=node.value)
    if node.right_child:
        go_down_the_tree(node.right_child, min=node.value, max=max)


def main():
    # values = [6, 0, 9, 3, 2, 4, 10, 9, 6, 10]
    values = [6, 0, 9, 3, 2, 4, 10, 9, 6, 10]
    print(values)
    tree = AVL_Tree(values)

    go_down_the_tree(tree.root, None, None)


if __name__ == "__main__":
    main()
