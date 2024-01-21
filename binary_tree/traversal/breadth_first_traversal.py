from binary_tree.traversal.abstract_traversal import AbstractTraversal
from collections import deque


class BreadthFirstTraversal(AbstractTraversal):
    """
    Class for performing breadth-first traversal on a binary tree.
    """

    def traverse(self, root):
        """
        Traverses a binary tree in a breadth-first manner.
        """
        if root is not None:
            queue = deque()
            queue.append(root)

            while queue:
                node = queue.popleft()
                node.visit()

                if node.get_left() is not None:
                    queue.append(node.get_left())

                if node.get_right() is not None:
                    queue.append(node.get_right())
