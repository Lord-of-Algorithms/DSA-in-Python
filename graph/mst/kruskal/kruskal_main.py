"""
Demonstrates the use of Kruskal's algorithm to find the minimum spanning tree (MST) of a graph.
This module highlights how Kruskal's algorithm is particularly suited for graphs represented as a list of edges,
as it processes edges by increasing weight, irrespective of their position in the graph. This edge list representation
is used because Kruskal's algorithm does not require direct access to the graph's adjacency structure, making it
efficient and straightforward for calculating the MST in graphs where edge connectivity is the primary concern.
"""

from graph.edge import Edge
from graph.mst.kruskal.union_find import UnionFind
from graph.vertex import Vertex


def build_mst(vertices, edges):
    """
    Constructs the minimum spanning tree (MST) for a graph represented by vertices and edges.
    Assumes that the graph is connected.

    :param vertices: List of vertices in the graph.
    :param edges: List of edges in the graph, where each edge has a source, destination, and weight.
    :return: List of edges that form the minimum spanning tree.
    """
    if not vertices:
        raise ValueError("Vertex list cannot be None or empty.")
    if not edges:
        raise ValueError("Edge list cannot be None or empty.")

    # Sorting edges by weight
    edges.sort(key=lambda edge: edge.get_weight())

    uf = UnionFind(vertices)
    mst = []

    for edge in edges:
        if uf.find(edge.source) != uf.find(edge.destination):
            mst.append(edge)
            uf.union(edge.source, edge.destination)
            # Check if the number of edges in MST is equal to
            # the number of vertices - 1
            if len(mst) == len(vertices) - 1:
                break

    return mst


def demo_kruskal_algorithm():
    # Initialize vertices
    a, b, c, d = Vertex("A"), Vertex("B"), Vertex("C"), Vertex("D")
    vertices = [a, b, c, d]

    edges = [
        Edge(a, b, 1),
        Edge(d, b, 2),
        Edge(b, c, 3),
        Edge(a, d, 4),
        Edge(d, c, 5)
    ]

    mst = build_mst(vertices, edges)
    print("MST:", [f"{edge}" for edge in mst])


if __name__ == "__main__":
    demo_kruskal_algorithm()
