from abc import ABC, abstractmethod


class AbstractTraversal(ABC):
    """
    Abstract base class for implementing different traversal strategies on a binary tree.
    """

    @abstractmethod
    def traverse(self, root):
        """
        Performs traversal of a binary tree.

        :param root: The root node of the tree to traverse.
        """
        pass
