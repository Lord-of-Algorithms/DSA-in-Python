class Vertex:
    """
    Represents a vertex in a graph.
    """

    def __init__(self, label):
        self.label = label

    def __eq__(self, other):
        return self.label == other.label if isinstance(other, Vertex) else False

    def __hash__(self):
        return hash(self.label)

    def __str__(self):
        return self.label
