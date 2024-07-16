class UnionFind:
    """
    Implements the union-find data structure (also known as disjoint-set).
    This implementation uses path compression in the find operation.
    """

    def __init__(self, vertices):
        """
        Initializes the UnionFind structure with a list of initial vertices.
        Each vertex is initially its own set with a rank of 0.

        :param vertices: List of vertex instances to be included in the union-find structure.
        """
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in vertices}

    def find(self, vertex):
        """
        Finds the representative (root) of the set containing the specified vertex
        using path compression to flatten the structure of the tree.

        :param vertex: Vertex whose set representative is to be found.
        :return: The representative of the set containing the vertex.
        """
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, x, y):
        """
        Unites the two sets that contain vertex 'root1' and 'root2'.
        Uses union by rank to optimize the tree structure.

        :param x: Vertex representing the first set.
        :param y: Vertex representing the second set.
        """
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            if self.rank[x_root] < self.rank[y_root]:
                self.parent[x_root] = y_root
            elif self.rank[x_root] > self.rank[y_root]:
                self.parent[y_root] = x_root
            else:
                self.parent[y_root] = x_root
                self.rank[x_root] += 1

    def connected(self, x, y):
        """
        Checks if two vertices are in the same set.

        :param x: Vertex to check.
        :param y: Vertex to check.
        :return: True if both vertices are in the same set, False otherwise.
        """
        return self.find(x) == self.find(y)
