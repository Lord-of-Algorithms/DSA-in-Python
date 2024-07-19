from graph.dijkstra.vertex_distance_priority_queue import VertexDistancePriorityQueue


class DijkstraAlgorithm:
    """
    Implements Dijkstra's algorithm for finding the shortest paths
    from a single source vertex to all other vertices in a graph
    with non-negative edge weights.
    """

    def __init__(self):
        self.predecessor_map = {}

    def compute_paths(self, graph, source):
        """
        Computes the shortest paths from the specified source vertex.

        :param graph: The graph on which to compute paths.
        :param source: The source vertex from which to compute paths.
        """
        if source not in graph.get_vertices():
            raise ValueError("Source vertex is not in the graph")

        distance_from_source_map = {}
        p_queue = VertexDistancePriorityQueue(graph.get_vertex_count())

        vertices = graph.get_vertices()
        for v in vertices:
            initial_distance = 0 if v == source else graph.INFINITY
            distance_from_source_map[v] = initial_distance
            self.predecessor_map[v] = None
            p_queue.add(v, initial_distance)

        while not p_queue.is_empty():
            closest_to_source = p_queue.poll_smallest()
            neighbors = graph.get_neighbors(closest_to_source)

            for n in neighbors:
                current_distance = distance_from_source_map[n]
                edge_weight = graph.get_edge_weight_between(closest_to_source, n)
                alternative_distance = distance_from_source_map[closest_to_source] + edge_weight
                if alternative_distance < current_distance:
                    p_queue.update(n, alternative_distance)
                    distance_from_source_map[n] = alternative_distance
                    self.predecessor_map[n] = closest_to_source

    def get_shortest_path_to(self, target):
        """
        Retrieves the shortest path from the source vertex
        to the specified target vertex.

        :param target: The target vertex to find the path to.
        :return: A list of vertices representing the shortest path.
        """
        path = []
        current = target
        while current is not None:
            path.append(current)
            current = self.predecessor_map[current]
        path.reverse()  # Reverse the path to get the right order
        return path

    def reset_state(self):
        """
        Resets the internal state of the algorithm, clearing stored predecessors.
        """
        self.predecessor_map.clear()
