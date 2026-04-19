"""
Demonstrates the Bellman-Ford algorithm for finding the shortest paths from a single source
vertex to all other vertices in a weighted directed graph.

Unlike Dijkstra's algorithm, Bellman-Ford correctly handles negative edge weights and can
detect negative weight cycles, which make shortest-path distances undefined.

Time complexity: O(V * E), where V is the number of vertices and E is the number of edges.
"""

from graph.weighted_edge import WeightedEdge
from graph.vertex import Vertex

INFINITY = float('inf')


def bellman_ford(vertices, edges, source):
    """
    Computes the shortest paths from a source vertex to all other vertices using the
    Bellman-Ford algorithm.

    :param vertices: List of all vertices in the graph.
    :param edges: List of all directed edges in the graph (may include negative weights).
    :param source: The starting vertex.
    :return: A tuple (distances, predecessors, has_negative_cycle) where distances is a dict
             mapping each vertex to its shortest distance from source, predecessors is a dict
             mapping each vertex to its predecessor on the shortest path, and has_negative_cycle
             is a bool indicating whether a negative weight cycle was detected.
    :raises ValueError: If the vertex or edge list is empty, or if the source is not in the graph.
    """
    if not vertices:
        raise ValueError("Vertex list cannot be empty.")
    if not edges:
        raise ValueError("Edge list cannot be empty.")
    if source not in vertices:
        raise ValueError("Source vertex is not in the vertex list.")

    # Step 1: Initialize distances — source is 0, everything else is infinity
    distances = {v: 0 if v == source else INFINITY for v in vertices}
    predecessors = {v: None for v in vertices}

    # Step 2: Relax all edges V-1 times
    updated = False
    for _ in range(len(vertices) - 1):
        updated = False

        for edge in edges:
            u, v, w = edge.source, edge.destination, edge.weight

            if distances[u] != INFINITY:
                new_dist = distances[u] + w
                if new_dist < distances[v]:
                    distances[v] = new_dist
                    predecessors[v] = u
                    updated = True

        # Early termination: if no edge was relaxed in this pass, distances are final
        # and no negative cycle exists — Step 3 can be skipped entirely.
        if not updated:
            break

    # Step 3: Detect negative weight cycles.
    # Only run if the loop completed all V-1 passes with updates still happening —
    # meaning distances never stabilised, which is the hallmark of a negative cycle.
    has_negative_cycle = False
    if updated:
        for edge in edges:
            u, v, w = edge.source, edge.destination, edge.weight
            if distances[u] != INFINITY and distances[u] + w < distances[v]:
                has_negative_cycle = True
                break

    return distances, predecessors, has_negative_cycle


def get_path(predecessors, target):
    """
    Reconstructs the shortest path from the source to the given target vertex
    by following the predecessor chain.

    :param predecessors: The predecessor dict produced by bellman_ford.
    :param target: The destination vertex.
    :return: A list of vertices from source to target, or an empty list if no path exists.
    """
    path = []
    v = target
    while v is not None:
        path.append(v)
        v = predecessors[v]
    path.reverse()
    return path


# -------------------------------------------------------------------------
# Demos
# -------------------------------------------------------------------------

def demonstrate_normal_graph():
    """
    Graph with a negative edge but no negative cycle.

    A --5--> B
    A --2--> D
    B --5--> C
    C --10-> F
    D --5--> E
    E --7--> F
    E --(-10)--> B
    """
    print("=== Example 1: Negative edge, no negative cycle ===")

    a, b, c, d, e, f = Vertex("A"), Vertex("B"), Vertex("C"), Vertex("D"), Vertex("E"), Vertex("F")
    vertices = [a, b, c, d, e, f]

    edges = [
        WeightedEdge(a, b, 5),
        WeightedEdge(a, d, 2),
        WeightedEdge(b, c, 5),
        WeightedEdge(c, f, 10),
        WeightedEdge(d, e, 5),
        WeightedEdge(e, f, 7),
        WeightedEdge(e, b, -10),
    ]

    distances, predecessors, has_negative_cycle = bellman_ford(vertices, edges, a)

    if has_negative_cycle:
        print("Negative cycle detected — distances are unreliable.")
    else:
        print("Shortest distances and paths from source A:")
        for v in vertices:
            path = get_path(predecessors, v)
            print(f"  {v}: distance={distances[v]}, path={[str(p) for p in path]}")


def demonstrate_negative_cycle_graph():
    """
    Graph containing a negative weight cycle (B -> C -> F -> E -> B, total weight = -6).

    A --5--> B
    A --2--> D
    B --3--> C
    C --4--> F
    D --5--> E
    F --2--> E
    E --(-15)--> B  <- closes the negative cycle
    """
    print("=== Example 2: Graph with a negative cycle ===")

    a, b, c, d, e, f = Vertex("A"), Vertex("B"), Vertex("C"), Vertex("D"), Vertex("E"), Vertex("F")
    vertices = [a, b, c, d, e, f]

    edges = [
        WeightedEdge(a, b, 5),
        WeightedEdge(a, d, 2),
        WeightedEdge(b, c, 3),
        WeightedEdge(c, f, 4),
        WeightedEdge(d, e, 5),
        WeightedEdge(f, e, 2),
        WeightedEdge(e, b, -15),  # Creates negative cycle: B -> C -> F -> E -> B
    ]

    distances, predecessors, has_negative_cycle = bellman_ford(vertices, edges, a)

    if has_negative_cycle:
        print("Negative cycle detected — no finite shortest paths exist.")
    else:
        print("No negative cycle found.")


if __name__ == "__main__":
    demonstrate_normal_graph()
    print()
    demonstrate_negative_cycle_graph()
