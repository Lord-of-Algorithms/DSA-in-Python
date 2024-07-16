from binary_tree.bst.avl.avl_node import AvlNode
from binary_tree.bst.bst_utils import search_recursive, min_value, handle_duplicate_key
from binary_tree.bst.abstract_tree import AbstractTree


def _get_height(node):
    """
    Calculates the height of a given node in the AVL tree.
    The height of a node is defined as the number of edges from the node to the deepest leaf.
    A leaf node has a height of 0, and an empty tree (or None node) has a height of -1.

    :param node: The node whose height is to be calculated.
    :return: The height of the node, or -1 if the node is None.
    """
    if node is None:
        return -1
    return node.height


def _get_balance(node):
    """
    Calculates the balance factor of a given node in the AVL tree.
    The balance factor is defined as the difference in height between the left and right subtrees.
    A balance factor greater than 1 indicates left-heavy imbalance,
    and a balance factor less than -1 indicates right-heavy imbalance.

    :param node: The node for which the balance factor is to be calculated.
    :return: The balance factor of the node. If the node is None, returns 0.
    """
    if node is None:
        return 0
    return _get_height(node.left) - _get_height(node.right)


def _update_height(node):
    node.height = max(_get_height(node.left), _get_height(node.right)) + 1


def _right_rotate(rotated_node):
    """
    Performs a right rotation on the given node.
    This rotation is used to correct the left-heavy imbalance in the AVL tree.
    In a right rotation, the left child of the rotated node becomes the new root
    of the subtree, and the original node becomes the right child of this new root.

    :param rotated_node: The node around which the right rotation is to be performed.
    :return: The new root of the subtree after the rotation.
    """
    new_root = rotated_node.left
    re_parented_node = new_root.right

    # Perform rotation
    new_root.right = rotated_node
    rotated_node.left = re_parented_node

    # Update heights of the rotated nodes
    _update_height(rotated_node)
    _update_height(new_root)

    return new_root


def _left_rotate(rotated_node):
    """
    Performs a left rotation on the given node.
    This rotation is used to correct the right-heavy imbalance in the AVL tree.
    In a left rotation, the right child of the rotated node becomes the new root
    of the subtree, and the original node becomes the left child of this new root.

    :param rotated_node: The node around which the left rotation is to be performed.
    :return: The new root of the subtree after the rotation.
    """
    new_root = rotated_node.right
    re_parented_node = new_root.left

    # Perform rotation
    new_root.left = rotated_node
    rotated_node.right = re_parented_node

    # Update heights of the rotated nodes
    _update_height(rotated_node)
    _update_height(new_root)

    return new_root


class AvlTree(AbstractTree):
    """
    Represents an AVL tree, a self-balancing binary search tree.
    """

    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, current, key):
        """
        Helper method to recursively insert a new key into the AVL tree.

        :param current: The root node of the current subtree.
        :param key: The key to insert.
        :return: The new root of the subtree after insertion.
        """
        if current is None:
            return AvlNode(key)

        if key < current.key:
            current.left = self._insert_recursive(current.left, key)
        elif key > current.key:
            current.right = self._insert_recursive(current.right, key)
        else:
            handle_duplicate_key(key)
            return current

        # Update height and calculate balance factor
        _update_height(current)
        balance = _get_balance(current)

        # Single Right Rotation
        if balance > 1 and key < current.left.key:
            return _right_rotate(current)

        # Single Left Rotation
        if balance < -1 and key > current.right.key:
            return _left_rotate(current)

        # Left-Right Rotation
        if balance > 1 and key > current.left.key:
            current.left = _left_rotate(current.left)
            return _right_rotate(current)

        # Right-Left Rotation
        if balance < -1 and key < current.right.key:
            current.right = _right_rotate(current.right)
            return _left_rotate(current)

        return current

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, current, key):
        """
        Helper method to recursively delete a key from the AVL tree.

        :param current: The root node of the current subtree.
        :param key: The key to delete.
        :return: The new root of the subtree after deletion.
        """
        if current is None:
            return None

        # Standard deletion in a binary search tree
        if key < current.key:
            current.left = self._delete_recursive(current.left, key)
        elif key > current.key:
            current.right = self._delete_recursive(current.right, key)
        else:
            # Case 1: Node with only one child or no child
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left

            # Case 2: Node with two children
            # Replace node's key with the minimum value from its right subtree
            current.key = min_value(current.right)
            # Delete the in-order successor (which has the minimum value)
            current.right = self._delete_recursive(current.right, current.get_key())

        # Update height and calculate balance factor
        _update_height(current)
        balance = _get_balance(current)

        # Single Right rotation
        if balance > 1 and _get_balance(current.left) >= 0:
            return _right_rotate(current)

        # Left-right rotation
        if balance > 1 and _get_balance(current.left) < 0:
            current.left = _left_rotate(current.left)
            return _right_rotate(current)

        # Single Left rotation
        if balance < -1 and _get_balance(current.right) <= 0:
            return _left_rotate(current)

        # Right-left rotation
        if balance < -1 and _get_balance(current.right) > 0:
            current.right = _right_rotate(current.right)
            return _left_rotate(current)

        return current

    def search(self, key):
        return search_recursive(self.root, key)
