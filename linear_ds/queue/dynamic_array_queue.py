from linear_ds.queue.queue import Queue


class DynamicArrayQueue(Queue):
    """
    Implements a circular queue using a dynamically resizable array.
    The queue automatically expands its capacity when it becomes full
    and shrinks when a significant portion of its capacity is unused.
    """

    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError("Capacity must be at least 1")
        self.data = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, element):
        if self.size == len(self.data):
            # Double the size of the array when
            # the queue is full
            self._resize(2 * len(self.data))
        self.rear = (self.rear + 1) % len(self.data)
        self.data[self.rear] = element
        self.size += 1

    def dequeue(self):
        """
        Removes and returns the element at the front of the queue.
        If the queue size drops to 1/4 of the array length, the capacity
        is reduced to half or a minimum of 10 to prevent excessive resizing.
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        item = self.data[self.front]
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1

        # Resize down if the queue is 1/4 full but not completely empty
        if 0 < self.size == len(self.data) // 4:
            self._resize(max(len(self.data) // 2, 10))  # Ensure the capacity doesn't get too small

        return item

    def _resize(self, new_capacity):
        """
        Resizes the internal storage of the queue to a new capacity.
        After resizing, the front is reset to 0, and rear is set to self.size - 1,
        maintaining the circular logic but within a new array context.
        """
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = \
                self.data[(self.front + i) % len(self.data)]
        self.data = new_data
        self.front = 0
        self.rear = self.size - 1

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data[self.front]

    def is_empty(self):
        return self.size == 0
