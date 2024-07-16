class UnionFind:
    """
    Implements the union-find data structure (also known as disjoint-set).
    This implementation uses path compression in the find operation.
    """

    def __init__(self, size):
        """
        Initializes the UnionFind structure with a specified number of elements.
        Each element is initially in its own set with a rank of zero.

        :param size: int - the number of elements in the UnionFind structure
        """
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, element):
        """
        Finds the representative (root) of the set containing 'element'
        and applies path compression.

        :param element: int - the element for which to find the set representative
        :return: int - the representative of the set containing 'element'
        """
        if self.parent[element] != element:
            self.parent[element] = self.find(self.parent[element])  # Path compression
        return self.parent[element]

    def union(self, x, y):
        """
        Merges the sets containing elements 'x' and 'y'.

        :param x: int - an element of the first set
        :param y: int - an element of the second set
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
        Determines whether two elements are in the same set.

        :param x: int - the first element
        :param y: int - the second element
        :return: bool - True if 'x' and 'y' are in the same set, False otherwise
        """
        return self.find(x) == self.find(y)
