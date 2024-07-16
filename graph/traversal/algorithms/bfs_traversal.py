from graph.traversal.algorithms.base_graph_traversal import BaseGraphTraversal


class BfsTraversal(BaseGraphTraversal):
    """
    Implements the Breadth-First Search (BFS) traversal algorithm for graphs.
    """

    def traverse(self, graph, start_vertex):
        queue = [start_vertex]
        self.visit(start_vertex)

        while queue:
            head = queue.pop(0)
            unvisited_neighbor = self.find_unvisited_neighbor(graph, head)
            while unvisited_neighbor:
                self.visit(unvisited_neighbor)
                queue.append(unvisited_neighbor)
                unvisited_neighbor = self.find_unvisited_neighbor(graph, head)
