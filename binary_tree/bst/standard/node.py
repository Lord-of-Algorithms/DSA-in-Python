from binary_tree.abstract_node import AbstractNode


class Node(AbstractNode):
    """
    Represents a node in a binary tree, adhering to the structure and behavior
    defined by the INode abstract base class.
    """

    def __init__(self, key):
        """
        Initialize a Node with a given key.

        :param key: The key value of the node.
        """
        self.key = key
        self.left = None
        self.right = None

    def get_key(self):
        """
        Gets the key value of this node.

        :return: The key of this node.
        """
        return self.key

    def get_left(self):
        """
        Gets the left child of this node.

        :return: The left child node.
        """
        return self.left

    def get_right(self):
        """
        Gets the right child of this node.

        :return: The right child node.
        """
        return self.right

    def visit(self):
        """
        Processes or visits the current node.
        In this implementation, it prints the node's key to the standard output.
        """
        print(self.key, end=" ")

    def __str__(self):
        """
        Returns a string representation of this node.

        :return: The string representation of the node.
        """
        return str(self.key)
