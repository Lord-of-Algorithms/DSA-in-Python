from graph.dijkstra.graph.dijkstra_graph import DijkstraGraph


class DijkstraMatrixGraph(DijkstraGraph):
    """
    Extends the DijkstraGraph abstract base class using an adjacency matrix to represent the graph.
    """

    def __init__(self, max_vertex_count):
        """
        Constructs a graph with a specified maximum number of vertices.
        """
        self.indices_map = {}
        self.adjacency_matrix = [[self.INFINITY for _ in range(max_vertex_count)] for _ in range(max_vertex_count)]
        self.vertices = []
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
            self.vertices.append(vertex)
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
        if weight < 0:
            raise ValueError("Edge weight cannot be negative.")

        source_index = self.indices_map[source]
        destination_index = self.indices_map[destination]

        self.adjacency_matrix[source_index][destination_index] = weight

    def get_vertices(self):
        return self.vertices.copy()

    def get_neighbors(self, vertex):
        if vertex not in self.indices_map:
            raise ValueError("Vertex does not exist in the graph")
        index = self.indices_map[vertex]
        neighbors = []
        for i in range(len(self.adjacency_matrix[index])):
            if self.adjacency_matrix[index][i] != self.INFINITY:
                for v, idx in self.indices_map.items():
                    if idx == i:
                        neighbors.append(v)
                        break
        return neighbors

    def get_edge_weight_between(self, source, destination):
        source_index = self.indices_map[source]
        destination_index = self.indices_map[destination]
        if source_index is None or destination_index is None:
            return self.INFINITY
        return self.adjacency_matrix[source_index][destination_index]

    def get_vertex_count(self):
        return self.current_vertex_count
