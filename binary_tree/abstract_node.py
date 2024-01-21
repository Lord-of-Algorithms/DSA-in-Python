from abc import ABC, abstractmethod


class AbstractNode(ABC):
    """
    Abstract base class representing a node in a binary tree.
    """

    @abstractmethod
    def get_key(self):
        """
        Gets the key value of this node.
        """
        pass

    @abstractmethod
    def get_left(self):
        """
        Gets the left child of this node.

        :return: The left child node.
        """
        pass

    @abstractmethod
    def get_right(self):
        """
        Gets the right child of this node.

        :return: The right child node.
        """
        pass

    @abstractmethod
    def visit(self):
        """
        Processes or visits the current node.
        """
        pass
