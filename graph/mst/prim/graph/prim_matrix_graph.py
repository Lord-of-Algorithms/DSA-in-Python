from graph.edge import Edge
from graph.mst.prim.graph.prim_graph import PrimGraph


class PrimMatrixGraph(PrimGraph):
    """
    Implements the PrimGraph using an adjacency matrix to represent the graph.
    """

    NO_EDGE = float('inf')  # Use infinity to represent no edge

    def __init__(self, max_vertex_count):
        """
        Constructs a graph with a specified maximum number of vertices.
        """
        self.indices_map = {}
        self.adjacency_matrix = [[self.NO_EDGE for _ in range(max_vertex_count)] for _ in range(max_vertex_count)]
        self.max_vertices = max_vertex_count
        self.current_vertex_count = 0

    def add_vertex(self, vertex):
        """
        Adds a vertex to the graph. Each vertex is indexed to correspond with the adjacency matrix.
        """
        if vertex is None:
            raise ValueError("Vertex cannot be None.")
        if self.current_vertex_count >= self.max_vertices:
            raise ValueError("Maximum vertices limit reached.")
        if vertex not in self.indices_map:
            self.indices_map[vertex] = self.current_vertex_count
            self.current_vertex_count += 1

    def set_edge(self, source, destination, weight):
        """
        Sets or updates the weight of the edge between the given source and destination vertices.
        """
        if source is None or destination is None:
            raise ValueError("Source or destination vertex cannot be None.")
        if source == destination:
            raise ValueError("Cannot add an edge from a vertex to itself.")
        if source not in self.indices_map or destination not in self.indices_map:
            raise ValueError("One or both vertices do not exist in the graph.")

        source_index = self.indices_map[source]
        destination_index = self.indices_map[destination]

        self.adjacency_matrix[source_index][destination_index] = weight
        self.adjacency_matrix[destination_index][source_index] = weight  # For undirected graph

    def get_edges_for_source(self, source):
        """
        Retrieves a list of all edges originating from a specified vertex.
        """
        if source not in self.indices_map:
            raise ValueError("Vertex does not exist in the graph")

        index = self.indices_map[source]
        edges = []
        for i, weight in enumerate(self.adjacency_matrix[index]):
            if weight != self.NO_EDGE:
                edges.append(Edge(source, self.get_vertex_by_index(i), weight))
        return edges

    def get_vertex_by_index(self, index):
        """
        Retrieves a vertex based on its index from a mapping of vertices to indices.

        :param index: int - The index for which to find the corresponding vertex.
        :return: Vertex - The vertex associated with the given index, or None if not found.
        """
        for vertex, idx in self.indices_map.items():
            if idx == index:
                return vertex
        return None

    def get_vertex_count(self):
        return self.current_vertex_count

    def contains_vertex(self, vertex):
        return vertex in self.indices_map
