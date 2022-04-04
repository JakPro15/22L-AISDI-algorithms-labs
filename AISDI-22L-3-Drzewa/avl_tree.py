from bstree import Binary_Search_Tree_Node


class AVL_Tree:
    def __init__(self, values=None):
        self.root = AVL_Tree_Node(self)
        if values:
            for value in values:
                self.root.insert(value)
    
    def insert(self, value):
        self.root.insert(value)
    
    @staticmethod
    def node_to_string(result_lines, node, depth):
        if len(result_lines) <= depth:
            result_lines.append("")
        if node.value:
            result_lines[depth] += f"{node.value} "
        if node.left_tree:
            AVL_Tree.node_to_string(result_lines, node.left_tree, depth + 1)
        if node.right_tree:
            AVL_Tree.node_to_string(result_lines, node.right_tree, depth + 1)

    def to_string(self):
        result_lines = []
        AVL_Tree.node_to_string(result_lines, self.root, 0)
        return "\n".join(result_lines)


class AVL_Tree_Node(Binary_Search_Tree_Node):
    def __init__(self, parent, value=None):
        super().__init__(value)
        self.parent = parent
        self.balance_factor = 0

    def insert(self, value):
        # Insert like in BST
        if not self.value:
            self.value = value
        elif self.value == value:
            return
        elif value < self.value:
            if self.left_tree:
                self.left_tree.insert(value)
            else:
                self.left_tree = AVL_Tree_Node(self, value)
        elif self.right_tree:
            self.right_tree.insert(value)
        else:
            self.right_tree = AVL_Tree_Node(self, value)
        
        if isinstance(self.parent, AVL_Tree_Node):
            # Fix balance factor
            if self == self.parent.right_tree:
                self.parent.balance_factor += 1
            else:
                self.parent.balance_factor -= 1
        
            if self.parent.balance_factor == 2:
                if self.balance_factor > 0:
                    # Right-Right case - Left rotation needed
                    self._rotate_left()
                else:
                    # Right-Left case - Right-Left rotation needed
                    self._rotate_right_left()
            elif self.parent.balance_factor == -2:
                if self.balance_factor < 0:
                    # Left-Left case - Right rotation needed
                    self._rotate_right()
                else:
                    # Left-Right case - Left-Right rotation needed
                    self._rotate_left_right()

    def _rotate_left(self, set_factors=True):
        x = self.parent
        # Rebind the left child of self
        if self.left_tree:
            x.right_tree = self.left_tree
            self.left_tree.parent = x
        else:
            x.right_tree = None

        # Rotate self with X
        if isinstance(x.parent, AVL_Tree_Node):
            if x == x.parent.left_tree:
                x.parent.left_tree = self
            else:
                x.parent.right_tree = self
            self.parent = x.parent
            x.parent = self
            self.left_tree = x
        else:
            x.parent.root = self
            self.parent = x.parent
            x.parent = self
            self.left_tree = x

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
        if self.right_tree:
            x.left_tree = self.right_tree
            self.right_tree.parent = x
        else:
            x.left_tree = None

        # Rotate self with X
        if isinstance(x.parent, AVL_Tree_Node):
            if x == x.parent.left_tree:
                x.parent.left_tree = self
            else:
                x.parent.right_tree = self
            self.parent = x.parent
            x.parent = self
            self.right_tree = x
        else:
            x.parent.root = self
            self.parent = x.parent
            x.parent = self
            self.right_tree = x

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
        y = self.right_tree

        # First rotate Y left...
        y._rotate_left(False)
        # ...then rotate Y right
        y._rotate_right(False)

        # Fix balance factors
        if y.balance_factor == 0:
            x.balance_factor = 0
            self.balance_factor = 0
        elif y.balance_factor > 0:
            x.balance_factor = 1
            self.balance_factor = 0
        else:
            x.balance_factor = 0
            self.balance_factor = -1

    def _rotate_right_left(self):
        x = self.parent
        y = self.left_tree

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
