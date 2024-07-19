from typing import List


class VertexDistance:
    """
    Holds vertex and its associated distance. This helps manage the mapping of vertices
    to their current shortest distances as known during the execution of Dijkstra's algorithm.
    """

    def __init__(self, vertex, distance):
        self.vertex = vertex
        self.distance = distance


class VertexDistancePriorityQueue:
    """
    A priority queue specifically designed for Dijkstra's algorithm that manages vertices according to their distances.
    This implementation is simple and primarily for educational purposes to demonstrate the management of vertices in a
    non-optimized priority queue. The queue maintains vertices in order of their distance from the source.
    Each time a vertex is removed, it ensures the vertex with the smallest distance is selected next.
    """

    def __init__(self, max_size):
        """
        Constructs a priority queue with a specified maximum size.

        :param max_size: the maximum number of elements the queue can hold
        """
        if max_size <= 0:
            raise ValueError("Maximum size must be greater than 0")
        self.max_size = max_size
        self.vertex_distances: List[VertexDistance] = []
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

    def add(self, vertex, distance):
        """
        Adds a vertex along with its distance to the queue in a sorted order based on the distance.

        :param vertex: the vertex to add
        :param distance: the distance of the vertex from the source
        """

        if self.is_full():
            raise Exception("Queue is full")

        # Find the correct position for the new element.
        position = 0
        while position < self.current_size and self.vertex_distances[position].distance > distance:
            position += 1

        # Insert the vertex-distance pair at the found position
        self.vertex_distances.insert(position, VertexDistance(vertex, distance))
        self.current_size += 1

    def poll_smallest(self):
        """
        Polls and returns the vertex from the queue that has the smallest distance.

        :return: the vertex with the smallest distance
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        self.current_size -= 1
        return self.vertex_distances.pop().vertex

    def update(self, vertex, distance):
        """
        Updates the distance of a specific vertex in the queue.

        :param vertex: the vertex whose distance needs to be updated
        :param distance: the new distance of the vertex
        """
        position = 0
        is_found = False
        while position < self.current_size:
            if self.vertex_distances[position].vertex == vertex:
                is_found = True
                break
            position += 1

        if not is_found:
            raise ValueError("Vertex not found")
        self.vertex_distances.pop(position)  # Remove the old element
        self.current_size -= 1
        self.add(vertex, distance)  # Add the new element maintaining order
