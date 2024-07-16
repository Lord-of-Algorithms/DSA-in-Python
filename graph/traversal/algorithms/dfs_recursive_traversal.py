from graph.traversal.algorithms.base_graph_traversal import BaseGraphTraversal


class DfsRecursiveTraversal(BaseGraphTraversal):
    """
    Implements the recursive Depth-First Search (DFS) traversal algorithm for graphs.
    """

    def traverse(self, graph, start_vertex):
        self._recursive_dfs(graph, start_vertex)

    def _recursive_dfs(self, graph, vertex):
        """
        Recursively performs depth-first search from the given vertex.
        """
        self.visit(vertex)
        unvisited_neighbor = self.find_unvisited_neighbor(graph, vertex)
        while unvisited_neighbor:
            self._recursive_dfs(graph, unvisited_neighbor)
            unvisited_neighbor = self.find_unvisited_neighbor(graph, vertex)
