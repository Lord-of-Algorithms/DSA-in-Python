from binary_tree.bst.bst_utils import handle_duplicate_key, search_recursive
from binary_tree.bst.abstract_tree import AbstractTree
from binary_tree.bst.red_black.rb_node import RbNode


def _transfer_color(source_node, target_node):
    """
    Transfers the color from one node to another in a Red-Black Tree.
    If source_node is red, target_node is set to red; if source_node is black, target_node is set to black.

    :param source_node: The node from which the color is copied.
    :param target_node: The node to which the color is applied.
    """
    if source_node.is_red():
        target_node.set_red()
    else:
        target_node.set_black()


class RedBlackTree(AbstractTree):
    """
    Represents a Red-Black Tree, a self-balancing binary search tree.
    In a Red-Black Tree, each node is colored either red or black and the tree
    maintains several balancing properties to ensure operations have logarithmic time complexity.
    """

    def __init__(self):
        """
        Initializes the tree with a sentinel node representing NIL.
        """
        self.NIL = RbNode.create_sentinel_node()
        self.root = self.NIL

    def get_root(self):
        return self.root

    def insert(self, key):
        """
        Inserts a new key into the Red-Black Tree.
        This method ensures that the tree maintains its properties after insertion.

        :param key: The key to be inserted.
        """
        new_node = RbNode(key, self.NIL)
        if self.root == self.NIL:
            self.root = new_node
            # Root is always black
            self.root.set_black()
            return
        current = self.root
        parent = self.NIL
        # Traverse the tree to find the appropriate insertion point.
        while current != self.NIL:
            parent = current
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                # Duplicate key found.
                handle_duplicate_key(key)
                return
        new_node.parent = parent
        # Attaching the new node to its parent.
        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node
        self._fix_insert(new_node)

    def _fix_insert(self, current):
        """
        Fixes the Red-Black Tree after an insertion.
        This method adjusts colors and performs rotations to maintain the tree's properties.

        :param current: The newly inserted node.
        """
        parent = current.parent
        while parent.is_red():
            grand_parent = parent.parent
            if parent == grand_parent.right:
                uncle = grand_parent.left
                # Case 1: The uncle is red
                if uncle.is_red():
                    uncle.set_black()
                    parent.set_black()
                    grand_parent.set_red()
                    current = grand_parent
                    # Reassign parent after changing 'current'
                    parent = current.parent
                else:
                    # Case 2: The uncle is black, the new node is a left child
                    # and its parent is a right child
                    if current == parent.left:
                        current = parent
                        self._rotate_right(current)
                        # Reassign parent and grandparent after changing 'current'
                        parent = current.parent
                        grand_parent = parent.parent
                    # Case 3: The uncle is black, the new node and
                    # its parent are both right children
                    parent.set_black()
                    grand_parent.set_red()
                    self._rotate_left(grand_parent)
            else:
                uncle = grand_parent.right
                # Case 1: The uncle is red
                if uncle.is_red():
                    uncle.set_black()
                    parent.set_black()
                    grand_parent.set_red()
                    current = grand_parent
                    # Reassign parent after changing 'current'
                    parent = current.parent
                else:
                    # Case 2: The uncle is black, the new node is a right child
                    # and its parent is a left child
                    if current == parent.right:
                        current = parent
                        self._rotate_left(current)
                        # Reassign parent and grandparent after changing 'current'
                        parent = current.parent
                        grand_parent = parent.parent
                    # Case 3: The uncle is black, the new node and
                    # its parent are both left children
                    parent.set_black()
                    grand_parent.set_red()
                    self._rotate_right(grand_parent)
            if current == self.root:
                break
        self.root.set_black()

    def _rotate_left(self, rotated_node):
        """
        Performs a left rotation on a given node.
        Left rotation is used to rebalance the tree during insertion and deletion operations.

        :param rotated_node: The node around which the left rotation will be performed.
        """
        new_root = rotated_node.right
        re_parented_node = new_root.left

        # Connect the re-parented node and rotated_node
        rotated_node.right = re_parented_node
        if re_parented_node != self.NIL:
            re_parented_node.parent = rotated_node

        # Attach the new root of subtree to the parent
        new_root.parent = rotated_node.parent
        if rotated_node.parent == self.NIL:
            self.root = new_root
        elif rotated_node == rotated_node.parent.left:
            rotated_node.parent.left = new_root
        else:
            rotated_node.parent.right = new_root

        # Connect the rotated_node and the new root of subtree
        new_root.left = rotated_node
        rotated_node.parent = new_root

    def _rotate_right(self, rotated_node):
        """
        Performs a right rotation on a given node.
        Right rotation is used to rebalance the tree during insertion and deletion operations.

        :param rotated_node: The node around which the right rotation will be performed.
        """
        new_root = rotated_node.left
        re_parented_node = new_root.right

        # Connect the re-parented node and rotated_node
        rotated_node.left = re_parented_node
        if re_parented_node != self.NIL:
            re_parented_node.parent = rotated_node

        # Attach the new root of subtree to the parent
        new_root.parent = rotated_node.parent
        if rotated_node.parent == self.NIL:
            self.root = new_root
        elif rotated_node == rotated_node.parent.right:
            rotated_node.parent.right = new_root
        else:
            rotated_node.parent.left = new_root

        # Connect the rotated_node and the new root of subtree
        new_root.right = rotated_node
        rotated_node.parent = new_root

    def delete(self, key):
        """
        Deletes a key from the Red-Black Tree.
        This method also ensures that the tree maintains its properties after deletion.

        :param key: The key to be deleted.
        """
        if self.root == self.NIL:
            print("The tree is empty.")
            return

        node_to_delete = self.root

        # Find the node to delete
        while node_to_delete != self.NIL and node_to_delete.key != key:
            if key < node_to_delete.key:
                node_to_delete = node_to_delete.left
            else:
                node_to_delete = node_to_delete.right

        if node_to_delete == self.NIL:
            print(f"Node with key {key} not found.")
            return

        # Handle node deletion based on the number of children

        # Node with zero or one child
        if node_to_delete.left == self.NIL or node_to_delete.right == self.NIL:
            is_deleting_node_black = node_to_delete.is_black
            replacer_node = self.NIL

            if node_to_delete.left == self.NIL:
                replacer_node = node_to_delete.right
                self._replace_subtree(node_to_delete, replacer_node)
            elif node_to_delete.right == self.NIL:
                replacer_node = node_to_delete.left
                self._replace_subtree(node_to_delete, replacer_node)

            if is_deleting_node_black:
                self._fix_delete(replacer_node)
        else:
            # Node with two children

            # Find the in-order successor (the leftmost node in the right subtree)
            successor = node_to_delete.right
            while successor.left != self.NIL:
                successor = successor.left

            # Remember the color of the successor and keep the link to its child
            is_initially_successor_black = successor.is_black
            successor_child = successor.right

            if successor.parent != node_to_delete:  # Successor is not a direct child of the deleting node
                # Replace the successor with its child
                self._replace_subtree(successor, successor.right)
                successor.right = node_to_delete.right

            # When successor.right is NIL, this line is ensuring that the NIL node's parent reference is updated.
            successor.right.parent = successor

            # Replace the node to be deleted with successor
            self._replace_subtree(node_to_delete, successor)
            successor.left = node_to_delete.left
            successor.left.parent = successor

            _transfer_color(node_to_delete, successor)

            if is_initially_successor_black:
                self._fix_delete(successor_child)

    def _replace_subtree(self, target_node, replacer_node):
        """
        Replaces one subtree rooted at 'target_node' with another subtree rooted at 'replacer_node'.
        This method is used to replace a node with its child.

        :param target_node: The root of the subtree that will be replaced.
        :param replacer_node: The root of the subtree that replaces the target subtree.
        """
        if target_node.parent == self.NIL:
            self.root = replacer_node
        elif target_node == target_node.parent.left:
            target_node.parent.left = replacer_node
        else:
            target_node.parent.right = replacer_node

        replacer_node.parent = target_node.parent

    def _fix_delete(self, current):
        """
        Restores the Red-Black Tree properties after the deletion of a node.
        This method addresses the 'double black' problem that arises when a black node is deleted
        or replaced by a black child. It rebalances the tree and ensures that the Red-Black Tree
        properties are maintained.

        :param current: The node starting from where the tree needs to be fixed.
        """
        while current != self.root and current.is_black:
            # The double black node 'current' is a left child
            if current == current.parent.left:
                # Sibling is a right child
                sibling = current.parent.right
                if sibling.is_red():
                    # Case 1: The sibling is red
                    sibling.set_black()
                    current.parent.set_red()
                    self._rotate_left(current.parent)
                    sibling = current.parent.right  # Update the sibling after rotation

                if sibling.left.is_black and sibling.right.is_black:
                    # Case 2: The sibling is black and has two black children
                    sibling.set_red()
                    current = current.parent
                else:
                    if sibling.right.is_black:
                        # Case 3: The sibling is black and has one red child (left) and one black child (right)
                        sibling.left.set_black()
                        sibling.set_red()
                        self._rotate_right(sibling)
                        sibling = current.parent.right  # Update the sibling after rotation

                    # Case 4: The sibling is black with a right red child
                    _transfer_color(current.parent, sibling)
                    current.parent.set_black()
                    sibling.right.set_black()
                    self._rotate_left(current.parent)
                    current = self.root  # Resolve the double black and exit the loop
            else:
                # Mirror operations if the double black node 'current' is a right child

                # Sibling is a left child
                sibling = current.parent.left
                if sibling.is_red():
                    # Case 1: The sibling is red
                    sibling.set_black()
                    current.parent.set_red()
                    self._rotate_right(current.parent)
                    sibling = current.parent.left  # Update the sibling after rotation

                if sibling.right.is_black and sibling.left.is_black:
                    # Case 2: The sibling is black and has two black children
                    sibling.set_red()
                    current = current.parent  # Propagate the double black problem up
                else:
                    if sibling.left.is_black:
                        # Case 3: The sibling is black and has one red child (right) and one black child (left)
                        sibling.right.set_black()
                        sibling.set_red()
                        self._rotate_left(sibling)
                        sibling = current.parent.left  # Update the sibling after rotation

                    # Case 4: The sibling is black with a left red child
                    _transfer_color(current.parent, sibling)
                    current.parent.set_black()
                    sibling.left.set_black()
                    self._rotate_right(current.parent)
                    current = self.root  # Resolve the double black and exit the loop

        current.set_black()  # Ensures the root of the tree is always black

    def search(self, key):
        return search_recursive(self.root, key)
