from graph.dijkstra.dijkstra_algorithm import DijkstraAlgorithm
from graph.dijkstra.graph.dijkstra_list_graph import DijkstraListGraph
from graph.dijkstra.graph.dijkstra_matrix_graph import DijkstraMatrixGraph
from graph.graph_representation import GraphRepresentation
from graph.vertex import Vertex


def create_graph(representation, vertices):
    if representation == GraphRepresentation.MATRIX:
        graph = DijkstraMatrixGraph(len(vertices))
    elif representation == GraphRepresentation.LIST:
        graph = DijkstraListGraph()
    else:
        raise ValueError(f"Unknown representation method: {representation}")
    for v in vertices:
        graph.add_vertex(v)
    return graph


def demo_dijkstra_algorithm():
    # Initialize vertices
    a, b, c, d = Vertex("A"), Vertex("B"), Vertex("C"), Vertex("D")

    # Create graph and add edges
    graph = create_graph(GraphRepresentation.MATRIX, [a, b, c, d])

    graph.set_edge(a, b, 13)
    graph.set_edge(c, b, 18)
    graph.set_edge(a, c, 13)
    graph.set_edge(b, d, 28)
    graph.set_edge(c, d, 85)

    dijkstra_algorithm = DijkstraAlgorithm()
    dijkstra_algorithm.compute_paths(graph, a)
    path = dijkstra_algorithm.get_shortest_path_to(d)
    print("Initial path to D:", [f"{vertex}" for vertex in path])

    # Update edges and recompute paths
    dijkstra_algorithm.reset_state()
    graph.set_edge(a, d, 10)  # Direct path added
    dijkstra_algorithm.compute_paths(graph, a)
    path = dijkstra_algorithm.get_shortest_path_to(d)
    print("Updated path to D with direct A to D:", [f"{vertex}" for vertex in path])

    dijkstra_algorithm.reset_state()
    graph.set_edge(a, b, 53)  # Increased weight A to B
    graph.set_edge(a, d, 100)  # Less optimal direct path A to D
    dijkstra_algorithm.compute_paths(graph, a)
    path = dijkstra_algorithm.get_shortest_path_to(d)
    print("Path after changing weights:", [f"{vertex}" for vertex in path])


if __name__ == "__main__":
    demo_dijkstra_algorithm()
