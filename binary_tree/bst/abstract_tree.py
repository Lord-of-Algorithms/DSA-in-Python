from abc import ABC, abstractmethod


class AbstractTree(ABC):
    """
    Abstract base class for a binary search tree.
    """

    @abstractmethod
    def get_root(self):
        """
        Retrieves the root node of the tree.

        :return: The root node of the tree.
        """
        pass

    @abstractmethod
    def insert(self, key):
        """
        Inserts a new node with the specified key into the tree.

        :param key: The key of the new node to be inserted.
        """
        pass

    @abstractmethod
    def delete(self, key):
        """
        Deletes the node with the specified key from the tree.

        :param key: The key of the node to be deleted.
        """
        pass

    @abstractmethod
    def search(self, key):
        """
        Searches for a node by its key.

        :param key: The key to search for.
        :return: The node with the specified key, or None if not found.
        """
        pass
