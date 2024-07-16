from graph.traversal.algorithms.base_graph_traversal import BaseGraphTraversal


class DfsTraversal(BaseGraphTraversal):
    """
    Implements the Depth-First Search (DFS) traversal algorithm for graphs.
    """

    def traverse(self, graph, start_vertex):
        stack = [start_vertex]
        self.visit(start_vertex)

        while stack:
            top = stack[-1]
            unvisited_neighbor = self.find_unvisited_neighbor(graph, top)
            if unvisited_neighbor is None:
                stack.pop()
            else:
                self.visit(unvisited_neighbor)
                stack.append(unvisited_neighbor)
