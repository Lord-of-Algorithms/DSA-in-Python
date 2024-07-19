from abc import ABC, abstractmethod


class Stack(ABC):
    """
    Abstract base class representing a stack data structure.
    """

    @abstractmethod
    def push(self, element):
        """
        Pushes an element onto the top of the stack.

        :param element: Element to be added to the top of the stack.
        """
        pass

    @abstractmethod
    def pop(self):
        """
        Removes and return the top element from the stack.
        """
        pass

    @abstractmethod
    def peek(self):
        """
        Returns the top element of the stack without.
        removing it.
        """
        pass

    @abstractmethod
    def is_empty(self):
        """
        Checks if the stack is empty.

        :return: True if stack is empty, False otherwise.
        """
        pass
