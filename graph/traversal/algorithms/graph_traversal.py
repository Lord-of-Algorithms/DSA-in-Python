from abc import ABC, abstractmethod


class GraphTraversal(ABC):
    """
    Defines the framework for graph traversal algorithms.
    """

    @abstractmethod
    def traverse(self, graph, start_vertex):
        """
        Traverses the graph starting from the specified vertex.
        """
        pass

    @abstractmethod
    def get_traversal_path(self):
        """
        Retrieves the path taken during the traversal as a list of visited vertices.
        :return: A list of vertices in the order they were visited during the traversal.
        """
        pass

    @abstractmethod
    def reset_state(self):
        """
        Resets the traversal state, including marking all vertices as unvisited.
        """
        pass
