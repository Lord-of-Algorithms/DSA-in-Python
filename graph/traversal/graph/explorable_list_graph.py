from graph.traversal.graph.explorable_graph import ExplorableGraph


class ExplorableListGraph(ExplorableGraph):
    """
    Represents an undirected and unweighted graph using an adjacency list representation.
    """

    def __init__(self):
        self._adjacency_list = []

    def add_vertex(self, vertex):
        if vertex is None:
            raise ValueError("Vertex cannot be None.")
        if vertex not in self._adjacency_list:
            self._adjacency_list[vertex] = []

    def set_edge(self, source, destination):
        if source is None or destination is None:
            raise ValueError("Source or destination vertex cannot be None.")
        if source == destination:
            raise ValueError("Cannot add an edge from a vertex to itself.")

        # Assuming source and destination are already in the adjacency list.
        self._adjacency_list[source].append(destination)
        self._adjacency_list[destination].append(source)

    def get_neighbors(self, vertex):
        return self._adjacency_list[vertex]
