from graph.edge import Edge
from graph.mst.prim.graph.prim_graph import PrimGraph


class PrimListGraph(PrimGraph):
    """
    Extends the PrimGraph abstract base class using an adjacency list to represent the graph.
    """

    def __init__(self):
        """
        Initializes an empty graph with an adjacency list representation.
        """
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        """
        Adds a vertex to the graph. Initializes an empty list for edges if the vertex is new.

        :param vertex: The vertex to add to the graph.
        """
        if vertex is None:
            raise ValueError("Vertex cannot be None.")
        self.adjacency_list.setdefault(vertex, [])

    def set_edge(self, source, destination, weight):
        """
        Adds or updates an edge between two specified vertices with the given weight.
        Since the edge properties are mutable in this implementation, updating an edge will
        involve removing the old edge and adding a new one.

        :param source: The source vertex of the edge.
        :param destination: The destination vertex of the edge.
        :param weight: int - The weight of the edge.
        """
        if source is None or destination is None:
            raise ValueError("Source or destination vertex cannot be None.")
        if source == destination:
            raise ValueError("Cannot add an edge from a vertex to itself.")
        if source not in self.adjacency_list or destination not in self.adjacency_list:
            raise ValueError("Both vertices must be added to the graph before connecting them.")

        # Handle updating of edges
        self.replace_or_update_edge(source, destination, weight)
        self.replace_or_update_edge(destination, source, weight)  # For undirected graphs

    def replace_or_update_edge(self, source, destination, weight):
        """
        Replaces an existing edge between specified source and destination vertices or
        adds a new edge if no existing edge is found.

        :param source: The source vertex of the edge.
        :param destination: The destination vertex of the edge.
        :param weight: int - The weight of the new edge.
        """
        edges = self.adjacency_list[source]
        for edge in edges:
            if edge.source == source and edge.destination == destination:
                edges.remove(edge)
                break
        edges.append(Edge(source, destination, weight))

    def get_edges_for_source(self, source):
        return self.adjacency_list.get(source, [])

    def get_vertex_count(self):
        return len(self.adjacency_list)

    def contains_vertex(self, vertex):
        return vertex in self.adjacency_list
