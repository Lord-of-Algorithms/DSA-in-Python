from abc import abstractmethod

from graph.traversal.algorithms.graph_traversal import GraphTraversal


class BaseGraphTraversal(GraphTraversal):
    """
    Base class for graph traversal algorithms. This class provides common functionalities
    needed for traversing a graph, such as marking vertices as visited and tracking the
    traversal path.
    """

    def __init__(self):
        self._visited_status_set = set()
        self._traversal_path = []

    def find_unvisited_neighbor(self, graph, vertex):
        """
        Finds an unvisited neighbor of the specified vertex in the given graph.

        :param graph: The graph containing the vertices.
        :param vertex: The vertex whose unvisited neighbor is to be found.
        :return: The first unvisited neighbor of the vertex, or None if all neighbors have been visited.
        """
        neighbors = graph.get_neighbors(vertex)
        for v in neighbors:
            if not self._is_visited(v):
                return v
        return None

    def _is_visited(self, vertex):
        """
        Checks if the specified vertex has been visited during the traversal.
        """
        return vertex in self._visited_status_set

    def visit(self, vertex):
        """
        Marks a vertex as visited and adds it to the traversal path.

        :param vertex: The vertex to mark as visited.
        """
        self._visited_status_set.add(vertex)
        self._traversal_path.append(vertex)

    def get_traversal_path(self):
        """
        Returns a copy of the traversal path.

        :return: A list of vertices representing the traversal path.
        """
        return self._traversal_path[:]

    def reset_state(self):
        """
        Resets the traversal state, clearing the visited status set and the traversal path.
        """
        self._visited_status_set.clear()
        self._traversal_path.clear()

    @abstractmethod
    def traverse(self, graph, start_vertex):
        """
        Abstract method that must be implemented to start the graph traversal.

        :param graph: The graph to traverse.
        :param start_vertex: The starting vertex for BFS traversal.
        """
        pass
