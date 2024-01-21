from collections import deque

from binary_tree.traversal.traversal_nature import TraversalNature


def _iterative_pre_order_traverse(root):
    """
    Iteratively traverses a binary tree in a pre-order manner.
    """
    if root is None:
        return
    stack = deque()
    stack.append(root)

    while stack:
        node = stack.pop()
        node.visit()

        # Push right and left children of the popped node to stack
        if node.get_right() is not None:
            stack.append(node.get_right())
        if node.get_left() is not None:
            stack.append(node.get_left())


def _recursive_pre_order_traverse(node):
    """
    Recursively traverses a binary tree in a pre-order manner.
    """
    if node is None:
        return

    node.visit()
    _recursive_pre_order_traverse(node.get_left())
    _recursive_pre_order_traverse(node.get_right())


class PreOrderTraversal:
    """
    Class for performing pre-order traversal on a binary tree.
    """

    def __init__(self, traversal_nature):
        self.traversal_nature = traversal_nature

    def traverse(self, root):
        if self.traversal_nature == TraversalNature.Iterative:
            _iterative_pre_order_traverse(root)
        else:
            _recursive_pre_order_traverse(root)
