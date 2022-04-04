class Binary_Search_Tree:
    def __init__(self, values):
        self.root = Binary_Search_Tree_Node()
        if values:
            for value in values:
                self.root.insert(value)

    def insert(self, value):
        self.root.insert(value)

    def delete(self, value):
        self.root = self.root.delete(value)


class Binary_Search_Tree_Node:
    def __init__(self, value=None):
        self.left_tree = None
        self.right_tree = None
        self.value = value

    def insert(self, value):
        if not self.value:
            self.value = value
            return
        elif self.value == value:
            return
        elif value < self.value:
            if self.left_tree:
                self.left_tree.insert(value)
                return
            self.left_tree = Binary_Search_Tree_Node(value)
            return
        if self.right_tree:
            self.right_tree.insert(value)
            return
        self.right_tree = Binary_Search_Tree_Node(value)

    def delete(self, value):
        if self is None:
            return self
        elif value < self.value:
            if self.left_tree:
                self.left_tree = self.left_tree.delete(value)
            return self
        elif value > self.value:
            if self.right_tree:
                self.right_tree = self.right_tree.delete(value)
            return self
        if self.right_tree is None:
            return self.left_tree
        if self.left_tree is None:
            return self.right_tree
        follower = self.right_tree
        while follower.left_tree:
            follower = follower.left_tree
        self.value = follower.value
        self.right_tree = self.right_tree.delete(follower.value)
        return self

    def search(self, value):
        if value == self.value:
            return self
        if value < self.value:
            if self.left_tree is None:
                return None
            self.left_tree.search(value)

        if value > self.value:
            if self.right_tree is None:
                return None
            self.right_tree.search(value)
