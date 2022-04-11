from math import ceil, log10


class Binary_Search_Tree:
    def __init__(self, values):
        self.root = Binary_Search_Tree_Node()
        if values:
            for value in values:
                self.root.insert(value)

    @property
    def height(self):
        return self.root.height()

    def max(self):
        return self.root.max()

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
                    if element.value:
                        searched_values.append(element)
        return searched_values

    def print_tree(self):
        if self.root.value is None:
            return
        digits = ceil(log10(self.max()))
        if digits % 2 == 0:
            digits += 1
        str_array = [" " * digits for x in range(2 ** (self.root.height()))]
        str_array[0] = "yeet"
        str_array[1] = f"{self.root.value: ^{digits}}"
        str_array = self.root.prepare_string(str_array, 1, digits)
        tree_strings = []
        h = self.root.height()
        while h > 0:
            tree_string = ""
            k = self.root.height() - h + 1
            tree_string += \
                " " * ceil((digits + 1) * (2 ** (k - 2)) - (digits + 1) / 2)
            for i in range(2 ** (h - 1), 2 ** h - 1):
                tree_string += str_array[i]
                tree_string += \
                    " " * (((2 ** (k - 1) - 1) * digits + 2 ** (k - 1)))
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

    def max(self):
        if self.value is None:
            return None
        elif self.right_tree:
            return self.right_tree.max()
        else:
            return self.value

    def insert(self, value):
        if self.value is None:
            self.value = value
        else:
            while value != self.value:
                if value < self.value:
                    if self.left_tree is None:
                        self.left_tree = Binary_Search_Tree_Node(value)
                        break
                    else:
                        self = self.left_tree
                elif value > self.value:
                    if self.right_tree is None:
                        self.right_tree = Binary_Search_Tree_Node(value)
                        break
                    else:
                        self = self.right_tree
                else:
                    break

    def delete(self, value):
        current = self
        previous = None
        while(current is not None and current.value is not None and
                current.value != value):
            previous = current
            if current.value < value:
                current = current.right_tree
            else:
                current = current.left_tree
        if current is None:
            return self
        if current.left_tree is None or current.right_tree is None:
            new_current = None
            if current.left_tree is None:
                new_current = current.right_tree
            else:
                new_current = current.left_tree
            if previous is None:
                return new_current
            if current == previous.left_tree:
                previous.left_tree = new_current
            else:
                previous.right_tree = new_current
            current = None
        else:
            parent = None
            follower = current.right_tree
            while follower.left_tree is not None:
                parent = follower
                follower = follower.left_tree
            if parent is not None:
                parent.left_tree = follower.right_tree
            else:
                current.right_tree = follower.right_tree
            current.value = follower.value
            follower = None
        return self

    def search(self, value):
        while (self is not None and self.value is not None and
                value != self.value):
            if value < self.value:
                self = self.left_tree
            else:
                self = self.right_tree
        return self

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

    def prepare_string(self, str_array, parent_index, digits):
        if self.left_tree:
            str_array[2 * parent_index] = f"{self.left_tree.value: ^{digits}}"
            self.left_tree.prepare_string(str_array, 2 * parent_index, digits)
        if self.right_tree:
            str_array[2 * parent_index + 1] = \
                f"{self.right_tree.value: ^{digits}}"
            self.right_tree.prepare_string(
                str_array, 2 * parent_index + 1, digits
            )
        return str_array
