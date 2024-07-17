class EdgePriorityQueue:
    """
    A priority queue specifically designed for storing and retrieving edges based on their weights,
    where the edge with the smallest weight is always prioritized for retrieval.
    """

    def __init__(self, max_size):
        """
        Constructs a priority queue with a specified maximum size.

        :param max_size: the maximum number of edges the queue can hold
        """
        if max_size <= 0:
            raise ValueError("Maximum size must be greater than 0")
        self.max_size = max_size
        self.edges = []
        self.current_size = 0

    def is_empty(self):
        """
        Checks if the queue is empty.

        :return: True if the queue has no elements, False otherwise
        """
        return self.current_size == 0

    def is_full(self):
        """
        Checks if the queue is full.

        :return: True if the queue is at maximum capacity, False otherwise
        """
        return self.current_size == self.max_size

    def add(self, edge):
        if self.is_full():
            raise Exception("Queue is full")

        # Find the correct position for the new edge.
        position = 0
        while position < self.current_size and self.edges[position].weight > edge.weight:
            position += 1

        # Insert the edge at the found position
        self.edges.insert(position, edge)
        self.current_size += 1

    def peek_smallest(self):
        """
        Retrieves, but does not remove, the smallest weight edge in the queue.

        :return: the smallest weight edge, or None if the queue is empty
        """
        return None if self.is_empty() else self.edges[-1]

    def poll_smallest(self):
        """
        Retrieves and removes the smallest weight edge in the queue.

        :return: the smallest weight edge
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        self.current_size -= 1
        return self.edges.pop()

    def replace(self, target_edge, replacement_edge):
        """
        Replaces one edge with another and maintains the queue's order.

        :param target_edge: the edge to be replaced
        :param replacement_edge: the new edge to insert
        """
        if target_edge not in self.edges:
            raise ValueError("Edge not found")
        index = self.edges.index(target_edge)
        self.edges.pop(index)  # Remove the old edge
        self.current_size -= 1
        self.add(replacement_edge)  # Add the new edge maintaining order

    def find_edge_with_destination(self, destination):
        """
        Finds an edge with a specific destination.

        :param destination: the vertex destination of the edge to find
        :return: the edge with the specified destination, or None if no such edge exists
        """
        for edge in self.edges:
            if edge.destination == destination:
                return edge
        return None
