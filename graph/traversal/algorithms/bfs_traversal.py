from graph.traversal.algorithms.base_graph_traversal import GraphTraversal


class BfsTraversal(GraphTraversal):
    """
    Implements the Breadth-First Search (BFS) traversal algorithm for graphs.
    """

    def __init__(self):
        self.traversal_path = []

    def traverse(self, graph, start_vertex):
        queue = [start_vertex]
        start_vertex.visit()
        self.traversal_path.append(start_vertex)

        while queue:
            head = queue.pop(0)
            adjacent = graph.find_unvisited_adjacent(head)
            while adjacent:
                adjacent.visit()
                self.traversal_path.append(adjacent)
                queue.append(adjacent)
                adjacent = graph.find_unvisited_adjacent(head)

    def get_traversal_path(self):
        return self.traversal_path

    def reset_state(self):
        for v in self.traversal_path:
            v.reset_visited_status()
        self.traversal_path.clear()
