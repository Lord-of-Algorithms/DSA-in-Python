"""
Demonstrates Kahn's algorithm for computing a topological ordering of a
directed acyclic graph (DAG).

A topological ordering is a linear sequence of all vertices such that for
every directed edge u -> v, vertex u appears before vertex v in the sequence.

Kahn's algorithm uses in-degrees — the number of incoming edges per vertex —
to determine which vertices are ready to be processed at each step.

Time complexity: O(V + E), where V is the number of vertices and E is the number of edges.
"""

from collections import deque
from graph.edge import Edge
from graph.vertex import Vertex


def topological_sort(vertices, edges):
    """
    Computes a topological ordering of the given DAG using Kahn's algorithm.

    :param vertices: List of all vertices in the graph.
    :param edges: List of all directed edges in the graph.
    :return: A tuple (order, has_cycle) where order is a list of vertices in
             topological order, and has_cycle is a bool indicating whether a
             cycle was detected.
    :raises ValueError: If the vertex list is None or empty, or if the edge list is None.
    """
    if not vertices:
        raise ValueError("Vertex list cannot be None or empty.")
    if edges is None:
        raise ValueError("Edge list cannot be None.")

    # Step 1: Compute in-degrees and build adjacency list from the edge list
    in_degree = {v: 0 for v in vertices}
    adjacency = {v: [] for v in vertices}

    for edge in edges:
        source = edge.source
        destination = edge.destination

        adjacency[source].append(destination)
        in_degree[destination] = in_degree[destination] + 1

    # Step 2: Enqueue all vertices with in-degree 0 — they have no dependencies
    queue = deque()
    for v in vertices:
        if in_degree[v] == 0:
            queue.append(v)

    # Step 3: Process the queue
    result = []
    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        for neighbor in adjacency[vertex]:
            in_degree[neighbor] = in_degree[neighbor] - 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Cycle detection: if not all vertices were processed, a cycle exists
    has_cycle = len(result) != len(vertices)
    return result, has_cycle


def print_result(result, has_cycle):
    if has_cycle:
        print("Cycle detected — topological sort is not possible.")
    else:
        print(f"Topological order: {[str(v) for v in result]}")


def demonstrate_dag():
    """
    A directed acyclic graph representing a simple dependency structure.

        A --> B
        A --> C
        B --> D
        C --> D
        D --> E
    """
    print("=== Example 1: Directed acyclic graph ===")

    a = Vertex("A")
    b = Vertex("B")
    c = Vertex("C")
    d = Vertex("D")
    e = Vertex("E")

    vertices = [a, b, c, d, e]
    edges = [
        Edge(a, b),
        Edge(a, c),
        Edge(b, d),
        Edge(c, d),
        Edge(d, e),
    ]

    result, has_cycle = topological_sort(vertices, edges)
    print_result(result, has_cycle)


def demonstrate_cyclic_graph():
    """
    A graph containing a cycle (B -> C -> D -> B), making topological sort impossible.

        A --> B
        B --> C
        C --> D
        D --> B  <- closes the cycle
    """
    print("=== Example 2: Graph with a cycle ===")

    a = Vertex("A")
    b = Vertex("B")
    c = Vertex("C")
    d = Vertex("D")

    vertices = [a, b, c, d]
    edges = [
        Edge(a, b),
        Edge(b, c),
        Edge(c, d),
        Edge(d, b),  # Creates cycle: B -> C -> D -> B
    ]

    result, has_cycle = topological_sort(vertices, edges)
    print_result(result, has_cycle)


if __name__ == "__main__":
    demonstrate_dag()
    print()
    demonstrate_cyclic_graph()
