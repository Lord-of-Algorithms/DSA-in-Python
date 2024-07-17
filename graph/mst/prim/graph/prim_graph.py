from abc import abstractmethod
from typing import Optional, List

from graph.vertex import Vertex
from graph.weighted_graph import WeightedGraph


class PrimGraph(WeightedGraph):
    """
    Extends the functionality of a basic weighted graph to provide methods
    specifically useful for implementing Prim's algorithm.
    """

    @abstractmethod
    def get_edges_for_source(self, source_vertex) -> Optional[List[Vertex]]:
        """
        Retrieves a list of all edges originating from a specified vertex.
        """
        pass

    @abstractmethod
    def contains_vertex(self, vertex):
        """
        Checks if a specific vertex is part of the graph.

        :return: True if the vertex is present in the graph, False otherwise
        """
        pass

    @abstractmethod
    def get_vertex_count(self):
        """
        Returns the total number of vertices in the graph.
        """
        pass
