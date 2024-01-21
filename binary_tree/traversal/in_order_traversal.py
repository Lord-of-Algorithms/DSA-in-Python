from collections import deque

from binary_tree.traversal.traversal_nature import TraversalNature


def _iterative_in_order_traverse(root):
    """
    Iteratively traverses a binary tree in an in-order manner.
    """
    if root is None:
        return
    stack = deque()
    node = root

    while stack or node is not None:
        if node is not None:
            stack.append(node)
            node = node.get_left()
        else:
            node = stack.pop()
            node.visit()
            node = node.get_right()


def _recursive_in_order_traverse(node):
    """
    Recursively traverses a binary tree in an in-order manner.
    """
    if node is None:
        return

    _recursive_in_order_traverse(node.get_left())
    node.visit()
    _recursive_in_order_traverse(node.get_right())


class InOrderTraversal:
    """
    Class for performing in-order traversal on a binary tree.
    """

    def __init__(self, traversal_nature):
        self.traversal_nature = traversal_nature

    def traverse(self, root):
        if self.traversal_nature == TraversalNature.Iterative:
            _iterative_in_order_traverse(root)
        else:
            _recursive_in_order_traverse(root)
