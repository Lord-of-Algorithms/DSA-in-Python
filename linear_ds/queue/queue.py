from abc import ABC, abstractmethod


class Queue(ABC):
    """
    Abstract base class for a queue.
    """

    @abstractmethod
    def enqueue(self, element):
        """
        Inserts an element at the rear of the queue.
        """
        pass

    @abstractmethod
    def dequeue(self):
        """
        Removes the element at the front of the queue
        and returns it.
        """
        pass

    @abstractmethod
    def peek(self):
        """
        Returns the element at the front of the
        queue without removing it.
        """
        pass

    @abstractmethod
    def is_empty(self):
        """
        Checks if the queue is empty.

        return: True if the queue is empty, False otherwise.
        """
        pass
