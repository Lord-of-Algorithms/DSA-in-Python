from binary_tree.abstract_node import AbstractNode


class RbNode(AbstractNode):
    """
    Represents a node in a Red-Black Tree.
    Each node contains a key, links to left and right children, and a parent node.
    The node also has a color (red or black) and a flag indicating if it's a sentinel node.
    """

    def __init__(self, key=None, sentinel=None):
        if key is not None:
            self.key = key
            self.left = sentinel
            self.right = sentinel
            self.parent = sentinel
            self.is_black = False
            self.is_sentinel = False
        else:
            # Sentinel node constructor
            self.is_sentinel = True
            self.set_black()

    @classmethod
    def create_sentinel_node(cls):
        """
        Factory method to create a sentinel node.
        Sentinel nodes are used to represent external None leaves and the root's parent in the Red-Black Tree.
        Sentinel nodes are always black.
        """
        node = cls()
        return node

    def is_red(self):
        """
        Checks if the node is red.

        :return: True if the node is red, False if the node is black.
        """
        return not self.is_black

    def is_black(self):
        """
        Checks if the node is black.

        :return: True if the node is black, False if the node is red.
        """
        return self.is_black

    def set_black(self):
        """
        Sets the node's color to black.
        """
        self.is_black = True

    def set_red(self):
        """
        Sets the node's color to red.
        """
        self.is_black = False

    def get_key(self):
        return self.key

    def get_left(self):
        if self.left is not None and not self.left.is_sentinel:
            return self.left
        else:
            return None

    def get_right(self):
        if self.right is not None and not self.right.is_sentinel:
            return self.right
        else:
            return None

    def visit(self):
        print(self.key, end=" ")

    def __str__(self):
        if self.is_red():
            return f"\033[31m{self.key}\033[0m"  # ANSI Red
        return str(self.key)
