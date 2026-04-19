class Edge:
    """
    Represents an unweighted directed edge between two vertices.
    """

    def __init__(self, source, destination):
        """
        Initializes an Edge with a source and a destination.

        :param source: Vertex - The source vertex of the edge.
        :param destination: Vertex - The destination vertex of the edge.
        """
        self.source = source
        self.destination = destination

    def __eq__(self, other):
        return (isinstance(other, Edge) and
                self.source == other.source and
                self.destination == other.destination)

    def __hash__(self):
        return hash((self.source, self.destination))

    def __str__(self):
        return f"{self.source}{self.destination}"
