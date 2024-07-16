from abc import ABC, abstractmethod

from graph.graph import Graph


class UnweightedGraph(Graph, ABC):
    """
    Represents an unweighted graph capable of adding edges.
    """

    @abstractmethod
    def set_edge(self, source_vertex, destination_vertex):
        """
        Adds an unweighted edge between two vertices in the graph.

        :param source_vertex: The source vertex of the edge.
        :param destination_vertex: The destination vertex of the edge.
        """
        pass
