from graph.edge import Edge


class WeightedEdge(Edge):
    """
    Represents a weighted directed edge between two vertices.
    """

    def __init__(self, source, destination, weight):
        """
        Initializes a WeightedEdge with a source, a destination, and a weight.

        :param source: Vertex - The source vertex of the edge.
        :param destination: Vertex - The destination vertex of the edge.
        :param weight: int - The weight of the edge.
        """
        super().__init__(source, destination)
        self.weight = weight

    def get_weight(self):
        """
        Returns the weight of the edge.
        """
        return self.weight

    def __eq__(self, other):
        return (isinstance(other, WeightedEdge) and
                self.source == other.source and
                self.destination == other.destination and
                self.weight == other.weight)

    def __hash__(self):
        return hash((self.source, self.destination, self.weight))

    def __str__(self):
        return f"{self.source}{self.destination} ({self.weight})"
