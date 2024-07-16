from unionfind.union_find import UnionFind


def demo_union_find():
    # Initialize UnionFind with 10 elements
    uf = UnionFind(10)

    # Perform some union operations
    uf.union(0, 1)
    uf.union(2, 3)
    uf.union(4, 5)
    uf.union(6, 7)
    uf.union(7, 8)
    uf.union(0, 9)
    uf.union(5, 9)

    # Output the root of each element to show which set they belong to
    for i in range(10):
        print(f"Element {i} is in set: {uf.find(i)}")

    # Check if two elements are in the same set
    print("Elements 2 and 3 are in the same set:", uf.connected(2, 3))
    print("Elements 0 and 8 are in the same set:", uf.connected(0, 8))
    print("Elements 1 and 6 are in the same set:", uf.connected(1, 6))


if __name__ == '__main__':
    demo_union_find()
