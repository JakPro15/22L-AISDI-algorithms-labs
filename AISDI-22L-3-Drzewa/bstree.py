class Binary_Search_Tree:
    def __init__(self, values):
        self.root = Binary_Search_Tree_Node()
        if values:
            for value in values:
                self.root.insert(value)
        self.height = self.root.height()

    def insert(self, values):
        if values:
            for value in values:
                self.root.insert(value)

    def delete(self, values):
        if values:
            for value in values:
                if self.root:
                    self.root = self.root.delete(value)

    def search(self, values):
        searched_values = []
        if values:
            for value in values:
                if self.root.search(value):
                    searched_values.append(self.root.search(value))
        return searched_values

    def print_tree(self):
        strings_array = ["     " for x in range(2 ** (self.root.height()))]
        strings_array[0] = "yeet"
        strings_array = self.root.prepare_string(strings_array, 1)


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
            return self.left_tree.search(value)

        if value > self.value:
            if self.right_tree is None:
                return None
            return self.right_tree.search(value)

    def height(self):
        if self.left_tree and self.right_tree:
            tree_height = max(
                self.left_tree.height(),
                self.right_tree.height()
                )
        elif self.left_tree:
            tree_height = self.left_tree.height()
        elif self.right_tree:
            tree_height = self.right_tree.height()
        else:
            tree_height = 0
        return tree_height + 1

    def prepare_string(self, strings_array, parent_index):
        strings_array[2 * parent_index] = f"{self.left_tree.value: ^5}"
        strings_array[2 * parent_index + 1] = f"{self.right_tree.value: ^5}"
        if self.left_tree:
            self.left_tree.prepare_string(strings_array, 2 * parent_index)
        if self.right_tree:
            self.right_tree.prepare_string(strings_array, 2 * parent_index + 1)
        return strings_array
