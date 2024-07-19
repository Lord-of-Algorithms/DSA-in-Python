from abc import ABC, abstractmethod
from typing import List

from graph.vertex import Vertex
from graph.weighted_graph import WeightedGraph


class DijkstraGraph(WeightedGraph):
    """
    Abstract base class for a graph structure that can be used with Dijkstra's algorithm.
    """

    # Represents a value considered as "infinite distance," used when there is no direct path between two vertices.
    INFINITY = float('inf')

    @abstractmethod
    def get_vertices(self) -> List[Vertex]:
        """
        Retrieves a list of all vertices in the graph.

        :return: List of all vertices.
        """
        pass

    @abstractmethod
    def get_neighbors(self, vertex) -> List[Vertex]:
        """
        Retrieves a list of neighboring vertices to a specified vertex. Neighbors are
        those vertices that are directly connected by an edge from the specified vertex.

        :param vertex: The vertex for which to find neighbors.
        :return: List of neighboring vertices.
        """
        pass

    @abstractmethod
    def get_edge_weight_between(self, source, destination) -> int:
        """
        Retrieves the weight of the edge between two specified vertices.
        If no edge exists, this method returns a value that signifies no connection.

        :param source: The source vertex.
        :param destination: The destination vertex.
        :return: The weight of the edge or INFINITY if no direct edge exists.
        """
        pass

    @abstractmethod
    def get_vertex_count(self):
        """
        Retrieves the count of vertices in the graph.

        :return: Total number of vertices in the graph.
        """
        pass
