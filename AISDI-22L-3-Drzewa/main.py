from avl_tree import AVL_Tree


def main():
    values = list(range(10))
    tree = AVL_Tree(values)
    print(tree.to_string())


if __name__ == "__main__":
    main()
