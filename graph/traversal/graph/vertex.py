class Vertex:
    """
    Represents a vertex in a graph.
    """
    def __init__(self, label):
        self.label = label
        self.visited = False

    def visit(self):
        """
        Marks this vertex as visited.
        """
        self.visited = True

    def reset_visited_status(self):
        """
        Resets the visited status of this vertex, marking it as unvisited.
        """
        self.visited = False

    def __str__(self):
        return self.label
