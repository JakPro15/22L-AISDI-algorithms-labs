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
                        if self.root is None:
                            self.root = AVL_Tree_Node(self, None, None)

    def search(self, values):
        searched_values = []
        if values:
            for value in values:
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
            self._insert_rebalance()

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
        if self.value is None:
            return None
        if value == self.value:
            return self
        if value < self.value:
            if self.left_child is None:
                return None
            return self.left_child.search(value)

        if value > self.value:
            if self.right_child is None:
                return None
            return self.right_child.search(value)

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
