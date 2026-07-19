class MinHeap:
    """A binary min-heap backed by a fixed-capacity array.

    A heap is a *complete* binary tree — every level is full except
    possibly the last, which fills left to right — that satisfies the
    *heap property*: every parent is less than or equal to its children.
    As a result the smallest value is always at the root.

    Because the tree is complete it maps directly onto an array with no
    gaps, so no node objects or references are needed. For the node at
    index ``i``:

      * its parent is at ``(i - 1) // 2``,
      * its left child at ``2 * i + 1``,
      * its right child at ``2 * i + 2``.

    All operations run in place. ``insert`` and ``extract_min`` are
    ``O(log n)``; ``peek_min`` is ``O(1)``.
    """

    def __init__(self, capacity):
        """Create an empty heap that can hold up to ``capacity`` values."""
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self._heap = [0] * capacity
        self._size = 0

    def is_empty(self):
        """Return True if the heap holds no values."""
        return self._size == 0

    def is_full(self):
        """Return True if the heap has no room for another value."""
        return self._size == len(self._heap)

    def size(self):
        """Return the number of values currently in the heap."""
        return self._size

    @staticmethod
    def _parent(i):
        return (i - 1) // 2

    @staticmethod
    def _left_child(i):
        return 2 * i + 1

    @staticmethod
    def _right_child(i):
        return 2 * i + 2

    def _swap(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def peek_min(self):
        """Return the smallest value without removing it."""
        if self.is_empty():
            raise IndexError("Heap is empty")
        return self._heap[0]

    def insert(self, value):
        """Insert a value.

        The value is placed at the first free slot and then sifted up
        until the heap property is restored.
        """
        if self.is_full():
            raise OverflowError("Heap is full")
        self._heap[self._size] = value
        self._sift_up(self._size)
        self._size += 1

    def _sift_up(self, i):
        # Move node i up while it is smaller than its parent.
        while i > 0 and self._heap[i] < self._heap[self._parent(i)]:
            self._swap(i, self._parent(i))
            i = self._parent(i)

    def extract_min(self):
        """Remove and return the smallest value.

        The root is swapped with the last leaf, that leaf is dropped, and
        the new root is sifted down until the heap property is restored.
        """
        if self.is_empty():
            raise IndexError("Heap is empty")
        self._swap(0, self._size - 1)
        minimum = self._heap[self._size - 1]
        self._size -= 1
        if not self.is_empty():
            self._sift_down(0)
        return minimum

    def _sift_down(self, i):
        # Move node i down while it is larger than its smaller child. A
        # node with no left child is a leaf, so the sift stops there.
        while self._left_child(i) < self._size:
            smaller = self._left_child(i)
            right = self._right_child(i)
            if right < self._size and self._heap[right] < self._heap[smaller]:
                smaller = right
            if self._heap[i] <= self._heap[smaller]:
                break
            self._swap(i, smaller)
            i = smaller

    def delete(self, i):
        """Remove the value at index ``i``.

        The last leaf fills the gap and is then sifted up or down,
        depending on how it compares with its new parent, until the heap
        property is restored.
        """
        if i < 0 or i >= self._size:
            raise IndexError("No node at index {}".format(i))
        self._swap(i, self._size - 1)
        self._size -= 1
        if i == self._size:
            return  # removed the last leaf
        if i > 0 and self._heap[i] < self._heap[self._parent(i)]:
            self._sift_up(i)
        else:
            self._sift_down(i)
