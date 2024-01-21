from binary_tree.bst.bst_utils import handle_duplicate_key, min_value, search_recursive
from binary_tree.bst.abstract_tree import AbstractTree
from binary_tree.bst.standard.node import Node


class BinarySearchTreeRecursive(AbstractTree):
    """
    Implementation of a binary search tree with recursive methods.
    """

    def __init__(self):
        self.root = None

    def get_root(self):
        """
        Retrieves the root node of the tree.

        :return: The root node of the tree.
        """
        return self.root

    def insert(self, key):
        """
        Inserts a new node with the specified key into the tree.

        :param key: The key of the new node to be inserted.
        """
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, current, key):
        """
        Helper method to recursively insert a new node.

        :param current: The root of the subtree.
        :param key: The key of the new node to be inserted.
        :return: The modified subtree with the new node inserted.
        """
        if current is None:
            return Node(key)

        if key < current.key:
            current.left = self._insert_recursive(current.left, key)
        elif key > current.key:
            current.right = self._insert_recursive(current.right, key)
        else:
            handle_duplicate_key(key)

        return current

    def delete(self, key):
        """
        Deletes the node with the specified key from the tree.

        :param key: The key of the node to be deleted.
        """
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, current, key):
        if current is None:
            return None

        if key < current.key:
            current.left = self._delete_recursive(current.left, key)
        elif key > current.key:
            current.right = self._delete_recursive(current.right, key)
        else:
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left

            current.key = min_value(current.right)
            current.right = self._delete_recursive(current.right, current.key)

        return current

    def search(self, key):
        """
        Searches for a node by its key.

        :param key: The key to search for.
        :return: The node with the specified key, or None if not found.
        """
        return search_recursive(self.root, key)
