from graph.graph_representation import GraphRepresentation
from graph.mst.prim.edge_priority_queue import EdgePriorityQueue
from graph.mst.prim.graph.prim_list_graph import PrimListGraph
from graph.mst.prim.graph.prim_matrix_graph import PrimMatrixGraph
from graph.vertex import Vertex


def build_mst(graph, start_vertex):
    """
    Constructs the minimum spanning tree (MST) for a graph starting from a specified vertex.
    This method implements Prim's algorithm, which incrementally builds the MST by selecting
    the smallest weight edge leading to a vertex not yet in the MST.

    :param graph: The graph on which to build the MST.
    :param start_vertex: The starting vertex for the MST.
    :raises ValueError: If the start vertex is not part of the graph.
    :raises RuntimeError: If the graph is disconnected and cannot form an MST.
    """
    if not graph.contains_vertex(start_vertex):
        raise ValueError("Start vertex is not part of the graph.")

    vertex_count = graph.get_vertex_count()
    if vertex_count < 1:
        raise RuntimeError("Graph must contain at least one vertex.")

    p_queue = EdgePriorityQueue(vertex_count)
    current_vertex = start_vertex

    in_tree_set = set()
    mst = []

    while len(in_tree_set) < vertex_count - 1:
        in_tree_set.add(current_vertex)
        edges = graph.get_edges_for_source(current_vertex)

        for current_edge in edges:
            neighbour = current_edge.destination
            if neighbour not in in_tree_set:
                pq_edge = p_queue.find_edge_with_destination(neighbour)
                if pq_edge:
                    if pq_edge.weight > current_edge.weight:
                        p_queue.replace(pq_edge, current_edge)
                else:
                    p_queue.add(current_edge)

        if p_queue.is_empty():
            raise RuntimeError("Graph is disconnected, MST cannot be completed.")

        edge = p_queue.poll_smallest()
        current_vertex = edge.destination
        mst.append(edge)

    return mst


def create_graph(representation, vertices):
    if representation == GraphRepresentation.MATRIX:
        graph = PrimMatrixGraph(len(vertices))
    elif representation == GraphRepresentation.LIST:
        graph = PrimListGraph()
    else:
        raise ValueError(f"Unknown representation method: {representation}")
    for v in vertices:
        graph.add_vertex(v)
    return graph


def demo_prim_algorithm():
    # Initialize vertices
    a, b, c, d = Vertex("A"), Vertex("B"), Vertex("C"), Vertex("D")

    # Create graph and add edges
    graph = create_graph(GraphRepresentation.LIST, [a, b, c, d])

    graph.set_edge(a, b, 1)
    graph.set_edge(d, b, 2)
    graph.set_edge(b, c, 3)
    graph.set_edge(a, d, 4)
    graph.set_edge(d, c, 5)

    mst = build_mst(graph, a)
    print("MST:", [f"{edge}" for edge in mst])


if __name__ == "__main__":
    demo_prim_algorithm()
