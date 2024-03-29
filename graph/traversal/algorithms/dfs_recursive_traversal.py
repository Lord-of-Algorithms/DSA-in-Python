from graph.traversal.algorithms.base_graph_traversal import GraphTraversal


class DfsRecursiveTraversal(GraphTraversal):
    """
    Implements the recursive Depth-First Search (DFS) traversal algorithm for graphs.
    """

    def __init__(self):
        self.traversal_path = []

    def traverse(self, graph, start_vertex):
        self._recursive_dfs(graph, start_vertex)

    def _recursive_dfs(self, graph, vertex):
        vertex.visit()
        self.traversal_path.append(vertex)

        adjacent = graph.find_unvisited_adjacent(vertex)
        while adjacent:
            self._recursive_dfs(graph, adjacent)
            adjacent = graph.find_unvisited_adjacent(vertex)

    def get_traversal_path(self):
        return self.traversal_path

    def reset_state(self):
        for vertex in self.traversal_path:
            vertex.reset_visited_status()
        self.traversal_path.clear()
