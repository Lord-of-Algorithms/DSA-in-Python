from abc import ABC, abstractmethod


class Graph(ABC):
    """
    Represents a general graph structure. This class serves as a base for other
    specific graph classes that can extend or implement more complex behaviors,
    such as adding edges and querying graph properties.
    """

    @abstractmethod
    def add_vertex(self, vertex):
        """
        Adds a vertex to the graph.

        :param vertex: The vertex to add to the graph.
        """
        pass
