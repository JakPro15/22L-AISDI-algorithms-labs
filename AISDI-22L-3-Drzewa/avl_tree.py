class AVL_Tree:
    def __init__(self, values=None):
        self.root = AVL_Tree_Node(self, None, None)
        if values:
            for value in values:
                self.root.insert(value)

    def insert(self, value):
        self.root.insert(value)

    def delete(self, values):
        if values:
            for value in values:
                if self.root:
                    element = self.root.search(value)
                    if element:
                        element.delete()

    def search(self, values):
        searched_values = []
        if values:
            for value in values:
                if self.root:
                    if self.root.search(value):
                        searched_values.append(self.root.search(value))
        return searched_values

    @staticmethod
    def node_to_string(result_lines, node, depth):
        if len(result_lines) <= depth:
            result_lines.append("")
        if node.value:
            result_lines[depth] += f"{node.value} "
        if node.left_child:
            AVL_Tree.node_to_string(result_lines, node.left_child, depth + 1)
        if node.right_child:
            AVL_Tree.node_to_string(result_lines, node.right_child, depth + 1)

    def to_string(self):
        result_lines = []
        AVL_Tree.node_to_string(result_lines, self.root, 0)
        return "\n".join(result_lines)


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
            self._rebalance()

    def _rebalance(self):
        # AVL Rebalancing
        a = self
        while isinstance(a.parent, AVL_Tree_Node):
            # Balance factors
            if a == a.parent.right_child:
                a.parent.balance_factor += 1
            else:
                a.parent.balance_factor -= 1

            # Rotations
            if a.parent.balance_factor == 2:
                if a.balance_factor > 0:
                    # Right-Right case - Left rotation needed
                    a._rotate_left()
                else:
                    # Right-Left case - Right-Left rotation needed
                    a._rotate_right_left()
                break
            elif a.parent.balance_factor == -2:
                if a.balance_factor < 0:
                    # Left-Left case - Right rotation needed
                    a._rotate_right()
                else:
                    # Left-Right case - Left-Right rotation needed
                    a._rotate_left_right()
                break
            elif a.parent.balance_factor == 0:
                break

            # Move to parent
            if isinstance(a.parent, AVL_Tree_Node):
                a = a.parent

    def insert(self, value):
        # Insert like in BST
        # AVL rebalancing done in constructor of the new node
        if self.value is None:
            self.value = value
        elif self.value == value:
            return
        elif value < self.value:
            if self.left_child:
                self.left_child.insert(value)
            else:
                AVL_Tree_Node(self, False, value)
        elif self.right_child:
            self.right_child.insert(value)
        else:
            AVL_Tree_Node(self, True, value)

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

    def delete(self, value):
        if value < self.value:
            if self.left_child:
                self.left_child.delete(value)
        elif value > self.value:
            if self.right_child:
                self.right_child.delete(value)
        else:
            if self.right_child is None:
                if self.parent.left_child == self:
                    self.parent.left_child = self.left_child
                    self.left_child.parent = self.parent
                else:
                    self.parent.right_child = self.left_child
                    self.left_child.parent = self.parent
            if self.left_child is None:
                if self.parent.left_child == self:
                    self.parent.left_child = self.right_child
                    self.right_child.parent = self.parent
                else:
                    self.parent.right_child = self.right_child
                    self.right_child.parent = self.parent
            follower = self.right_child
            while follower.left_child:
                follower = follower.left_child
            self.value = follower.value
            if follower.parent.left_child == follower:
                follower.parent.left_child = follower.right_child
                follower.right_child.parent = follower.parent
            else:
                follower.parent.right_child = follower.right_child
                follower.right_child.parent = follower.parent
