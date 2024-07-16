from abc import ABC, abstractmethod
from typing import Optional, List

from graph.unweighted_graph import UnweightedGraph
from graph.vertex import Vertex


class ExplorableGraph(UnweightedGraph, ABC):
    """
    Represents an unweighted graph capable of finding neighbor vertices.
    """

    @abstractmethod
    def get_neighbors(self, vertex) -> Optional[List[Vertex]]:
        """
        Retrieves a list of neighboring vertices to a specified vertex. Neighbors are
        those vertices that are directly connected by an edge from the specified vertex.
        """
        pass
