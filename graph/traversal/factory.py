from graph.traversal.graph.undirected_unweighted_list_graph import UndirectedUnweightedListGraph
from graph.traversal.graph.undirected_unweighted_matrix_graph import UndirectedUnweightedMatrixGraph
from graph.traversal.algorithms.bfs_traversal import BfsTraversal
from graph.traversal.algorithms.dfs_recursive_traversal import DfsRecursiveTraversal
from enum import Enum

from graph.traversal.algorithms.dfs_traversal import DfsTraversal


class GraphTraversalMethod(Enum):
    """
    Enumeration of graph traversal methods.
    """
    DFS = 1  # Depth-First Search traversal method.
    DFS_RECURSIVE = 2  # Depth-First Search traversal method implemented recursively.
    BFS = 3  # Breadth-First Search traversal method.


class GraphTraversalFactory:
    """
    Factory class for creating graph traversal instances.
    """

    @staticmethod
    def create_traversal(method):
        if method == GraphTraversalMethod.DFS:
            return DfsTraversal()
        elif method == GraphTraversalMethod.DFS_RECURSIVE:
            return DfsRecursiveTraversal()
        elif method == GraphTraversalMethod.BFS:
            return BfsTraversal()
        else:
            raise ValueError(f"Unknown traversal method: {method}")


class GraphRepresentation(Enum):
    """
    Enumeration of graph representations.
    """
    MATRIX = 0  # Graph represented using an adjacency matrix.
    LIST = 1  # Graph represented using an adjacency list.


class GraphFactory:
    """
    Factory class for creating graph instances based on different representations.
    """

    @staticmethod
    def create_graph(representation, vertices):
        if representation == GraphRepresentation.MATRIX:
            return UndirectedUnweightedMatrixGraph(vertices)
        elif representation == GraphRepresentation.LIST:
            return UndirectedUnweightedListGraph(vertices)
        else:
            raise ValueError(f"Unknown representation method: {representation}")
