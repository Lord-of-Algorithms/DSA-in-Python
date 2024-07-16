"""
This module demonstrates various graph traversal methods such as DFS, BFS, and recursive DFS.
It provides utility functions to create graphs and perform traversals, displaying the paths.
Functions in this module include graph creation, graph traversal initiation, and the setup of graph traversal methods
via an enumeration.
"""

from enum import Enum

from graph.graph_representation import GraphRepresentation
from graph.traversal.algorithms.bfs_traversal import BfsTraversal
from graph.traversal.algorithms.dfs_recursive_traversal import DfsRecursiveTraversal
from graph.traversal.algorithms.dfs_traversal import DfsTraversal
from graph.traversal.graph.explorable_list_graph import ExplorableListGraph
from graph.traversal.graph.explorable_matrix_graph import ExplorableMatrixGraph
from graph.vertex import Vertex


class GraphTraversalMethod(Enum):
    """
    Enumeration of graph traversal methods.
    """
    DFS = 1  # Depth-First Search traversal method.
    DFS_RECURSIVE = 2  # Depth-First Search traversal method implemented recursively.
    BFS = 3  # Breadth-First Search traversal method.


def create_traversal(method):
    if method == GraphTraversalMethod.DFS:
        return DfsTraversal()
    elif method == GraphTraversalMethod.DFS_RECURSIVE:
        return DfsRecursiveTraversal()
    elif method == GraphTraversalMethod.BFS:
        return BfsTraversal()
    else:
        raise ValueError(f"Unknown traversal method: {method}")


def create_graph(representation, vertices):
    if representation == GraphRepresentation.MATRIX:
        explorable_graph = ExplorableMatrixGraph(len(vertices))
    elif representation == GraphRepresentation.LIST:
        explorable_graph = ExplorableListGraph()
    else:
        raise ValueError(f"Unknown representation method: {representation}")
    for v in vertices:
        explorable_graph.add_vertex(v)
    return explorable_graph


def demo_traversal_algorithms():
    # Initialize vertices
    a, b, c, d = Vertex("A"), Vertex("B"), Vertex("C"), Vertex("D")

    # Create graph and add edges
    graph = create_graph(GraphRepresentation.MATRIX, [a, b, c, d])
    graph.set_edge(a, b)
    graph.set_edge(a, d)
    graph.set_edge(b, c)
    graph.set_edge(b, d)
    graph.set_edge(c, d)

    # Perform DFS traversal
    traversal = create_traversal(GraphTraversalMethod.DFS)
    traversal.traverse(graph, a)
    print("DFS Traversal Path:", [str(vertex) for vertex in traversal.get_traversal_path()])
    traversal.reset_state()

    # Perform recursive DFS traversal
    traversal = create_traversal(GraphTraversalMethod.DFS_RECURSIVE)
    traversal.traverse(graph, a)
    print("Recursive DFS Traversal Path:", [str(vertex) for vertex in traversal.get_traversal_path()])
    traversal.reset_state()

    # Perform BFS traversal
    traversal = create_traversal(GraphTraversalMethod.BFS)
    traversal.traverse(graph, a)
    print("BFS Traversal Path:", [str(vertex) for vertex in traversal.get_traversal_path()])


if __name__ == "__main__":
    demo_traversal_algorithms()
