class BinarySearchTree:
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
            self.left_tree = BinarySearchTree(value)
            return
        elif self.right_tree:
            self.right_tree.insert(value)
            return
        self.right_tree = BinarySearchTree(value)

    def give_min(self):
        min = self
        while min.left_tree is not None:
            min = min.left_tree
        return min.value

    def give_max(self):
        max = self
        while max.right_tree is not None:
            max = max.right_tree
        return max.value

    def delete(self, value):
        if self is None:
            return self
        elif value < self.value:
            self.left_tree = self.left_tree.delete(value)
        elif value > self.value:
            self.right_tree = self.right_tree.delete(value)
        elif self.right_tree is None:
            return self.left_tree
        elif self.left_tree is None:
            return self.right_tree
        follower = self.right_tree.give_min()
        self.right_tree = self.right_tree.delete(follower)
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
