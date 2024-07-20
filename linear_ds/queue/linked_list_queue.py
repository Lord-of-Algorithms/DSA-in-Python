from linear_ds.queue.queue import Queue


class LinkedListQueue(Queue):
    """
    Implements a queue using a singly linked list. This implementation allows for dynamic resizing
    without a fixed capacity.
    """

    class Node:
        """
        A private Node class for storing queue elements with a reference to the next node.
        """

        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        """
        Initialize the queue with front and rear pointers set to None.
        This configuration indicates an empty queue.
        """
        self.front = None
        self.rear = None

    def enqueue(self, element):
        new_node = self.Node(element)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        data = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.front.value

    def is_empty(self):
        return self.front is None
