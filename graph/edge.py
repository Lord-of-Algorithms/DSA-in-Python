class Edge:
    """
    Represents an edge in a graph, defined by a source vertex,
    a destination vertex, and a weight.
    """

    def __init__(self, source, destination, weight):
        """
        Initializes an Edge with a source, a destination, and a weight.

        :param source: Vertex - The source vertex of the edge.
        :param destination: Vertex - The destination vertex of the edge.
        :param weight: int - The weight of the edge.
        """
        self.source = source
        self.destination = destination
        self.weight = weight

    def get_weight(self):
        """
        Returns the weight of the edge.
        """
        return self.weight

    def __eq__(self, other):
        """
        Determines whether two edges are equal based on their source, destination, and weight.

        :param other: Edge - The edge to compare with this edge.
        :return: bool - True if both edges are equal, False otherwise.
        """
        return (self.source == other.source and
                self.destination == other.destination and
                self.weight == other.weight)

    def __hash__(self):
        """
        Returns the hash code of the edge, allowing it to be used in sets and dictionaries.
        """
        return hash((self.source, self.destination, self.weight))

    def __str__(self):
        """
        Returns a string representation of the edge.
        """
        return f"{self.source}{self.destination} ({self.weight})"
