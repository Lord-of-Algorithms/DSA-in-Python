from collections import deque

from binary_tree.traversal.traversal_nature import TraversalNature


def _iterative_post_order_traverse(root):
    """
    Iteratively traverses a binary tree in a post-order manner.
    """
    if root is None:
        return
    stack1 = deque()
    stack2 = deque()

    stack1.append(root)

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.get_left() is not None:
            stack1.append(node.get_left())
        if node.get_right() is not None:
            stack1.append(node.get_right())

    while stack2:
        stack2.pop().visit()


def _recursive_post_order_traverse(node):
    """
    Recursively traverses a binary tree in a post-order manner.
    """
    if node is not None:
        _recursive_post_order_traverse(node.get_left())
        _recursive_post_order_traverse(node.get_right())
        node.visit()


class PostOrderTraversal:
    """
    Class for performing post-order traversal on a binary tree.
    """

    def __init__(self, traversal_nature):
        self.traversal_nature = traversal_nature

    def traverse(self, root):
        if self.traversal_nature == TraversalNature.Iterative:
            _iterative_post_order_traverse(root)
        else:
            _recursive_post_order_traverse(root)
