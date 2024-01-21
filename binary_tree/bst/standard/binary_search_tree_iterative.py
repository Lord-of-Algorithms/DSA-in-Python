from binary_tree.bst.bst_utils import handle_duplicate_key
from binary_tree.bst.abstract_tree import AbstractTree
from binary_tree.bst.standard.node import Node


class BinarySearchTreeIterative(AbstractTree):
    """
    Implementation of a binary search tree with iterative methods.
    """

    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def insert(self, key):
        new_node = Node(key)
        # Handle the case of an empty tree.
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        parent = None

        # Traverse the tree to find the appropriate insertion point.
        while current is not None:
            parent = current
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                # Duplicate key found.
                handle_duplicate_key(key)
                return

        # Attaching the new node to its parent.
        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

    def delete(self, key):
        if self.root is None:
            print("The tree is empty.")
            return

        node_to_delete = self.root
        parent_node = None

        # Find the node to delete and its parent
        while node_to_delete is not None and node_to_delete.key != key:
            parent_node = node_to_delete
            if key < node_to_delete.key:
                node_to_delete = node_to_delete.left
            else:
                node_to_delete = node_to_delete.right

        if node_to_delete is None:
            print(f"Node with key {key} not found.")
            return

        # Check if node_to_delete is the root
        is_root_node = node_to_delete == self.root
        is_left_child = parent_node is not None and node_to_delete.key < parent_node.key

        # Case 1: Node is a leaf (no children)
        if node_to_delete.left is None and node_to_delete.right is None:
            if is_root_node:
                self.root = None
            elif is_left_child:
                parent_node.left = None
            else:
                parent_node.right = None
        # Case 2: Node has only one child
        elif node_to_delete.left is None or node_to_delete.right is None:
            child_node = node_to_delete.left if node_to_delete.left is not None else node_to_delete.right

            if is_root_node:
                self.root = child_node
            elif is_left_child:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
        # Case 3: Node has two children
        else:
            # Find the in-order successor (smallest in the right subtree)
            successor = node_to_delete.right
            successor_parent = node_to_delete
            while successor.left is not None:
                successor_parent = successor
                successor = successor.left

            # If the successor is not the direct right child of node_to_delete,
            # then handle the re-linking of the successor and its parent
            if successor != node_to_delete.right:
                # Re-link the left child of the successor's parent to the successor's right child
                successor_parent.left = successor.right

                # Link the right child of the node_to_delete to the successor
                successor.right = node_to_delete.right

            successor.left = node_to_delete.left

            # Replace node_to_delete with successor in its parent
            if is_root_node:
                self.root = successor
            elif is_left_child:
                parent_node.left = successor
            else:
                parent_node.right = successor

    def search(self, key):
        current = self.root
        while current is not None:
            if key == current.key:
                return current  # Node found
            current = current.left if key < current.key else current.right
        return None  # Key not found
