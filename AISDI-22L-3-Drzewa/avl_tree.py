from math import ceil, log10


class AVL_Tree:
    def __init__(self, values=None):
        self.root = AVL_Tree_Node(self, None, None)
        if values:
            for value in values:
                self.root.insert(value)

    @property
    def height(self):
        return self.root.height()

    def max(self):
        return self.root.max()

    def insert(self, value):
        self.root.insert(value)

    def delete(self, values):
        if values:
            for value in values:
                element = self.root.search(value)
                if element:
                    element.delete()
                    if self.root is None:
                        self.root = AVL_Tree_Node(self, None, None)

    def search(self, values):
        searched_values = []
        if values:
            for value in values:
                element = self.root.search(value)
                if element:
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
        self.root.prepare_string(str_array, 1, digits)
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


class AVL_Tree_Node:
    def __init__(self, parent, right: bool = None, value=None):
        self.left_child = None
        self.right_child = None
        self.value = value
        self.parent = parent
        self.balance_factor = 0
        if right is not None:
            if right:
                self.parent.right_child = self
            else:
                self.parent.left_child = self
        # Fix balance factors if value was just inserted here
        if self.value is not None:
            self._insert_rebalance()

    def height(self):
        if self.left_child and self.right_child:
            child_height = max(
                self.left_child.height(),
                self.right_child.height()
                )
        elif self.left_child:
            child_height = self.left_child.height()
        elif self.right_child:
            child_height = self.right_child.height()
        else:
            child_height = 0
        return child_height + 1

    def max(self):
        if self.value is None:
            return None
        elif self.right_child:
            return self.right_child.max()
        else:
            return self.value

    def do_rotations(self):
        if self.balance_factor == 2:
            if self.right_child.balance_factor >= 0:
                # Right-Right case - Left rotation needed
                no_further_changes = (self.right_child.balance_factor == 0)
                self.right_child._rotate_left()
            else:
                # Right-Left case - Right-Left rotation needed
                no_further_changes = False
                self.right_child._rotate_right_left()
        elif self.balance_factor == -2:
            if self.left_child.balance_factor <= 0:
                # Left-Left case - Right rotation needed
                no_further_changes = (self.left_child.balance_factor == 0)
                self.left_child._rotate_right()
            else:
                # Left-Right case - Left-Right rotation needed
                no_further_changes = False
                self.left_child._rotate_left_right()
        return no_further_changes

    def _insert_rebalance(self):
        # AVL Rebalancing - Insert case
        a = self
        while isinstance(a.parent, AVL_Tree_Node):
            # Balance factors
            if a == a.parent.right_child:
                a.parent.balance_factor += 1
            else:
                a.parent.balance_factor -= 1

            # Rotations
            if a.parent.balance_factor in {-2, 2}:
                a.parent.do_rotations()
                break
            elif a.parent.balance_factor == 0:
                break

            # Move to parent
            if isinstance(a.parent, AVL_Tree_Node):
                a = a.parent

    def _delete_rebalance(self, from_right):
        # AVL Rebalancing - Delete case
        a = self
        rotated = False
        while True:
            # Move one step up now if a rotation just happened
            if rotated:
                if isinstance(a.parent, AVL_Tree_Node):
                    if a.parent.right_child == a:
                        from_right = True
                    else:
                        from_right = False
                    a = a.parent
                    rotated = False
                    continue
                else:
                    break

            # Balance factors
            if from_right:
                a.balance_factor -= 1
            else:
                a.balance_factor += 1

            # Rotations
            if a.balance_factor in {-2, 2}:
                rotated = True
                if a.do_rotations():
                    break
            elif a.balance_factor != 0:
                break

            # Move to parent
            if isinstance(a.parent, AVL_Tree_Node):
                if a.parent.right_child == a:
                    from_right = True
                else:
                    from_right = False
                a = a.parent
            else:
                break

    def insert(self, value):
        # Insert like in BST
        # AVL rebalancing done in constructor of the new node
        if self.value is None:
            self.value = value
        else:
            while value != self.value:
                if value < self.value:
                    if self.left_child is None:
                        AVL_Tree_Node(self, False, value)
                        break
                    else:
                        self = self.left_child
                elif value > self.value:
                    if self.right_child is None:
                        AVL_Tree_Node(self, True, value)
                        break
                    else:
                        self = self.right_child
                else:
                    break

    def _rotate_left(self, set_factors=True):
        x = self.parent
        # Rebind the left child of self
        if self.left_child:
            x.right_child = self.left_child
            self.left_child.parent = x
        else:
            x.right_child = None

        # Rotate self with X
        if isinstance(x.parent, AVL_Tree_Node):
            if x == x.parent.left_child:
                x.parent.left_child = self
            else:
                x.parent.right_child = self
            self.parent = x.parent
            x.parent = self
            self.left_child = x
        else:
            x.parent.root = self
            self.parent = x.parent
            x.parent = self
            self.left_child = x

        if set_factors:
            # Fix balance factors
            if self.balance_factor == 0:
                x.balance_factor = 1
                self.balance_factor = -1
            else:
                x.balance_factor = 0
                self.balance_factor = 0

    def _rotate_right(self, set_factors=True):
        x = self.parent
        # Rebind the right child of self
        if self.right_child:
            x.left_child = self.right_child
            self.right_child.parent = x
        else:
            x.left_child = None

        # Rotate self with X
        if isinstance(x.parent, AVL_Tree_Node):
            if x == x.parent.left_child:
                x.parent.left_child = self
            else:
                x.parent.right_child = self
            self.parent = x.parent
            x.parent = self
            self.right_child = x
        else:
            x.parent.root = self
            self.parent = x.parent
            x.parent = self
            self.right_child = x

        if set_factors:
            # Fix balance factors
            if self.balance_factor == 0:
                x.balance_factor = -1
                self.balance_factor = 1
            else:
                x.balance_factor = 0
                self.balance_factor = 0

    def _rotate_left_right(self):
        x = self.parent
        y = self.right_child

        # First rotate Y left...
        y._rotate_left(False)
        # ...then rotate Y right
        y._rotate_right(False)

        # Fix balance factors
        if y.balance_factor == 0:
            x.balance_factor = 0
            self.balance_factor = 0
        elif y.balance_factor > 0:
            x.balance_factor = 0
            self.balance_factor = -1
        else:
            x.balance_factor = 1
            self.balance_factor = 0
        y.balance_factor = 0

    def _rotate_right_left(self):
        x = self.parent
        y = self.left_child

        # First rotate Y right...
        y._rotate_right(False)
        # ...then rotate Y left
        y._rotate_left(False)

        # Fix balance factors
        if y.balance_factor == 0:
            x.balance_factor = 0
            self.balance_factor = 0
        elif y.balance_factor > 0:
            x.balance_factor = -1
            self.balance_factor = 0
        else:
            x.balance_factor = 0
            self.balance_factor = 1
        y.balance_factor = 0

    def search(self, value):
        if self.value is None:
            return None
        while (self is not None and value != self.value):
            if value < self.value:
                self = self.left_child
            else:
                self = self.right_child
        return self

    def delete(self):
        if self.right_child is None or self.right_child is None:
            self.delete_unconditional()
        else:
            follower = self.right_child
            while follower.left_child:
                follower = follower.left_child
            self.value = follower.value
            follower.delete_unconditional()

    def delete_unconditional(self):
        if self.right_child is None:
            child = self.left_child
        else:
            child = self.right_child

        if isinstance(self.parent, AVL_Tree):
            self.parent.root = child
            if child:
                child.parent = self.parent
        elif self.parent.left_child == self:
            self.parent.left_child = child
            if child:
                child.parent = self.parent
            self.parent._delete_rebalance(from_right=False)
        else:
            self.parent.right_child = child
            if child:
                child.parent = self.parent
            self.parent._delete_rebalance(from_right=True)

    def prepare_string(self, str_array, parent_index, digits):
        if self.left_child:
            str_array[2 * parent_index] = f"{self.left_child.value: ^{digits}}"
            self.left_child.prepare_string(str_array, 2 * parent_index, digits)
        if self.right_child:
            str_array[2 * parent_index + 1] = \
                f"{self.right_child.value: ^{digits}}"
            self.right_child.prepare_string(
                str_array, 2 * parent_index + 1, digits
            )
