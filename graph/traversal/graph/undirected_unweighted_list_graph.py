from typing import List

from graph.traversal.graph.base_unweighted_graph import UnweightedGraph
from graph.traversal.graph.vertex import Vertex


class UndirectedUnweightedListGraph(UnweightedGraph):
    def __init__(self, vertices: List[Vertex]):
        if not vertices:
            raise ValueError("Vertex list cannot be null or empty.")

        self.adjacency_list = {vertex: [] for vertex in vertices}

    def set_edge(self, source, destination):
        if source is None or destination is None:
            raise ValueError("Source or destination vertex cannot be null.")
        if source == destination:
            raise ValueError("Cannot add an edge from a vertex to itself.")

        # Assuming source and destination are already in the adjacency list.
        self.adjacency_list[source].append(destination)
        self.adjacency_list[destination].append(source)

    def find_unvisited_adjacent(self, visitable):
        neighbors = self.adjacency_list.get(visitable)
        if neighbors is None:
            raise ValueError("Vertex does not exist in the graph")

        for neighbor in neighbors:
            if not neighbor.visited:
                return neighbor
        return None
