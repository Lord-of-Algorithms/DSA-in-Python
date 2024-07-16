from graph.traversal.graph.explorable_graph import ExplorableGraph


class ExplorableMatrixGraph(ExplorableGraph):
    """
    Represents an undirected and unweighted graph using an adjacency matrix for storing edges.
    """

    def __init__(self, max_vertex_count):
        self._indices_map = {}
        self._adjacency_matrix = [[0] * max_vertex_count for _ in range(max_vertex_count)]
        self._max_vertices = max_vertex_count
        self._current_vertex_count = 0

    def add_vertex(self, vertex):
        if vertex is None:
            raise ValueError("Vertex cannot be None.")
        if self._current_vertex_count >= self._max_vertices:
            raise Exception("Maximum vertices limit reached.")
        if vertex not in self._indices_map:
            self._indices_map[vertex] = self._current_vertex_count
            self._current_vertex_count += 1

    def set_edge(self, source, destination):
        if source is None or destination is None:
            raise ValueError("Source or destination vertex cannot be None.")
        if source == destination:
            raise ValueError("Cannot add an edge from a vertex to itself.")
        if source not in self._indices_map or destination not in self._indices_map:
            raise ValueError("One or both vertices do not exist in the graph.")

        source_index = self._indices_map[source]
        destination_index = self._indices_map[destination]

        self._adjacency_matrix[source_index][destination_index] = 1
        self._adjacency_matrix[destination_index][source_index] = 1

    def get_neighbors(self, vertex):
        if vertex not in self._indices_map:
            raise ValueError("Vertex does not exist in the graph")
        index = self._indices_map[vertex]
        neighbors = []
        for i in range(len(self._adjacency_matrix[index])):
            if self._adjacency_matrix[index][i] == 1:
                for v, idx in self._indices_map.items():
                    if idx == i:
                        neighbors.append(v)
                        break
        return neighbors
