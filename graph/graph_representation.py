from enum import Enum


class GraphRepresentation(Enum):
    """
    Enumeration of graph representations.
    """
    MATRIX = 0  # Graph represented using an adjacency matrix.
    LIST = 1  # Graph represented using an adjacency list.
