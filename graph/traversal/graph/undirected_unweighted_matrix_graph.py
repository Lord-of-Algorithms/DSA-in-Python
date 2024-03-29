from typing import List, Dict, Optional

from graph.traversal.graph.base_unweighted_graph import UnweightedGraph
from graph.traversal.graph.vertex import Vertex


class UndirectedUnweightedMatrixGraph(UnweightedGraph):
    """
    Represents an undirected and unweighted graph using an adjacency matrix for storing edges.
    """

    def __init__(self, vertices: List[Vertex]):
        if not vertices:
            raise ValueError("Vertex list cannot be null or empty.")

        # Maps each vertex to its corresponding index in the adjacency matrix.
        self.indices_map: Dict[Vertex, int] = {vertex: i for i, vertex in enumerate(vertices)}
        # Represents the edges between vertices.
        self.adjacency_matrix: List[List[int]] = [[0 for _ in vertices] for _ in vertices]

    def set_edge(self, source, destination):
        if source is None or destination is None:
            raise ValueError("Source or destination vertex cannot be null.")
        if source == destination:
            raise ValueError("Cannot add an edge from a vertex to itself.")
        if source not in self.indices_map or destination not in self.indices_map:
            raise ValueError("One or both vertices do not exist in the graph.")

        source_index = self.indices_map[source]
        destination_index = self.indices_map[destination]

        self.adjacency_matrix[source_index][destination_index] = 1
        self.adjacency_matrix[destination_index][source_index] = 1

    def find_unvisited_adjacent(self, vertex):
        index = self.indices_map.get(vertex)
        if index is None:
            raise ValueError("Vertex does not exist in the graph")

        for i, edge in enumerate(self.adjacency_matrix[index]):
            if edge == 1:  # Check if there's an edge
                adjacent_vertex = self._get_vertex_by_index(i)  # Find the vertex by its index
                if adjacent_vertex is not None and not adjacent_vertex.visited:
                    return adjacent_vertex
        return None

    def _get_vertex_by_index(self, value: int) -> Optional[Vertex]:
        """
        Helper method to find a vertex by its index.
        """
        for vertex, index in self.indices_map.items():
            if index == value:
                return vertex
        return None
