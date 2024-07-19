from graph.dijkstra.graph.dijkstra_graph import DijkstraGraph
from graph.edge import Edge


def replace_or_update_edge(edges, source, destination, weight):
    """
    Replaces an existing edge between specified source and destination vertices or
    adds a new edge if no existing edge is found.
    This function modifies the edge list in place and does not return any value.
    """
    for edge in edges:
        if edge.source == source and edge.destination == destination:
            edges.remove(edge)
            break
    edges.append(Edge(source, destination, weight))


class DijkstraListGraph(DijkstraGraph):
    """
    Extends the DijkstraGraph abstract base class using an adjacency list representation.
    """

    def __init__(self):
        """
        Initializes an empty graph with an adjacency list representation.
        """
        self.adjacency_list = {}
        self.vertices = []

    def add_vertex(self, vertex):
        """
        Adds a vertex to the graph. Initializes an empty list for edges if the vertex is new.

        :param vertex: The vertex to add to the graph.
        """
        if vertex is None:
            raise ValueError("Vertex cannot be None.")
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            self.vertices.append(vertex)

    def set_edge(self, source, destination, weight):
        """
        Adds or updates a directed edge from a source vertex to a destination vertex with a specified weight.

        :param source: the source vertex of the edge
        :param destination: the destination vertex of the edge
        :param weight: the weight of the edge
        """
        if source is None or destination is None:
            raise ValueError("Source or destination vertex cannot be None.")
        if source == destination:
            raise ValueError("Cannot add an edge from a vertex to itself.")
        if source not in self.adjacency_list or destination not in self.adjacency_list:
            raise ValueError("One or both vertices do not exist in the graph.")
        if weight < 0:
            raise ValueError("Edge weight cannot be negative.")

        edges = self.adjacency_list[source]
        replace_or_update_edge(edges, source, destination, weight)

    def get_vertices(self):
        return self.vertices.copy()

    def get_neighbors(self, vertex):
        return [e.destination for e in self.adjacency_list.get(vertex, [])]

    def get_edge_weight_between(self, source, destination):
        for edge in self.adjacency_list.get(source, []):
            if edge.destination == destination:
                return edge.weight
        return self.INFINITY

    def get_vertex_count(self):
        return len(self.vertices)
