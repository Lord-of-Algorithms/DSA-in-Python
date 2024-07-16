from abc import ABC, abstractmethod

from graph.graph import Graph


class WeightedGraph(Graph, ABC):
    """
    Represents a weighted graph capable of adding edges.
    """

    @abstractmethod
    def set_edge(self, source_vertex, destination_vertex, weight):
        """
        Adds a weighted edge between two vertices in the graph.

        :param source_vertex: The source vertex of the edge.
        :param destination_vertex: The destination vertex of the edge.
        :param weight: The weight of the edge.
        """
        pass
