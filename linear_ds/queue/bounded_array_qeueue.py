from linear_ds.queue.queue import Queue


class BoundedArrayQueue(Queue):
    """
    A fixed-size circular queue implementation using an array.
    """

    def __init__(self, capacity):
        """
        Initializes the queue with a given capacity.

        :param capacity: The maximum number of items that the queue can hold.
        :raises ValueError: If the capacity is less than 1.
        """
        if capacity < 1:
            raise ValueError("Capacity must be at least 1")
        self.data = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, element):
        if self.is_full():
            raise Exception("Queue is full")
        self.rear = (self.rear + 1) % len(self.data)
        self.data[self.rear] = element
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        value = self.data[self.front]
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data[self.front]

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        """
        Checks if the queue is full.

        :return: True if the queue is full, False otherwise.
        """
        return self.size == len(self.data)
