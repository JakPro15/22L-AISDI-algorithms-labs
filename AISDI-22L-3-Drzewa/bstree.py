from math import ceil


class Binary_Search_Tree:
    def __init__(self, values):
        self.root = Binary_Search_Tree_Node()
        if values:
            for value in values:
                self.root.insert(value)

    @property
    def height(self):
        return self.root.height()

    def insert(self, values):
        if values:
            for value in values:
                self.root.insert(value)

    def delete(self, values):
        if values:
            for value in values:
                self.root = self.root.delete(value)
                if self.root is None:
                    self.root = Binary_Search_Tree_Node()

    def search(self, values):
        searched_values = []
        if values:
            for value in values:
                element = self.root.search(value)
                if element:
                    searched_values.append(element)
        return searched_values

    def print_tree(self):
        str_array = ["     " for x in range(2 ** (self.root.height()))]
        str_array[0] = "yeet"
        str_array[1] = f"{self.root.value: ^5}"
        str_array = self.root.prepare_string(str_array, 1)
        tree_strings = []
        h = self.root.height()
        while h > 0:
            tree_string = ""
            k = self.root.height() - h + 1
            tree_string += " " * ceil(6 * (2 ** (k - 2)) - 3)
            for i in range(2 ** (h - 1), 2 ** h - 1):
                tree_string += str_array[i]
                tree_string += " " * (((2 ** (k - 1) - 1) * 5 + 2 ** (k - 1)))
            tree_string += str_array[2 ** h - 1]
            tree_string += "\n"
            tree_strings.append(tree_string)
            h -= 1
        length = len(tree_strings)
        while length > 0:
            print(tree_strings[length - 1])
            length -= 1


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
        if self.value is None:
            return self
        if value < self.value:
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
        if self.value is None:
            return None
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

    def prepare_string(self, str_array, parent_index):
        if self.left_tree:
            str_array[2 * parent_index] = f"{self.left_tree.value: ^5}"
            self.left_tree.prepare_string(str_array, 2 * parent_index)
        if self.right_tree:
            str_array[2 * parent_index + 1] = f"{self.right_tree.value: ^5}"
            self.right_tree.prepare_string(str_array, 2 * parent_index + 1)
        return str_array
