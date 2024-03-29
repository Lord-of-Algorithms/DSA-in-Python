from graph.traversal.algorithms.base_graph_traversal import GraphTraversal


class DfsTraversal(GraphTraversal):
    """
    Implements the Depth-First Search (DFS) traversal algorithm for graphs.
    """

    def __init__(self):
        self.traversal_path = []

    def traverse(self, graph, start_vertex):
        stack = [start_vertex]
        start_vertex.visit()
        self.traversal_path.append(start_vertex)

        while stack:
            top = stack[-1]
            adjacent = graph.find_unvisited_adjacent(top)
            if adjacent is None:
                stack.pop()
            else:
                adjacent.visit()
                self.traversal_path.append(adjacent)
                stack.append(adjacent)

    def get_traversal_path(self):
        return self.traversal_path

    def reset_state(self):
        for v in self.traversal_path:
            v.reset_visited_status()
        self.traversal_path.clear()
