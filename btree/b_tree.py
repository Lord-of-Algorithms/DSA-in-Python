class _Node:
    """A B-tree node: its keys in ascending order and, unless it is a leaf,
    one more child than it has keys."""

    def __init__(self):
        self.keys = []
        self.children = []

    def is_leaf(self):
        return len(self.children) == 0


class BTree:
    """A B-tree of distinct integer keys.

    A B-tree is a balanced search tree whose nodes hold several keys at
    once. The keys inside a node are kept in ascending order, and a node
    holding ``k`` keys, unless it is a leaf, has ``k + 1`` children: one
    for each gap between two keys, and one at either end. Every key in a
    child lies in the range its gap describes.

    The size of the nodes is set by the *maximum degree* ``m``: the most
    children a node may have. From it follow the two rules every node
    obeys:

      * at most ``m - 1`` keys — one more and the node splits;
      * at least ``ceil(m / 2) - 1`` keys, for every node but the root —
        one fewer and the node borrows a key from a neighbour or merges
        with one.

    Every leaf sits at the same depth. A new key joins a leaf that already
    exists, and the tree grows taller only when its root splits, which
    adds a level above the whole tree at once. Deleting runs the same
    machinery backwards, and the tree grows shorter only when a merge
    empties the root.

    ``contains``, ``insert`` and ``delete`` each walk one path from the
    root to a leaf and back, so all three are ``O(log n)``.
    """

    def __init__(self, max_degree):
        """Create an empty B-tree whose nodes may have up to
        ``max_degree`` children."""
        if max_degree < 3:
            raise ValueError("Max degree must be at least 3")
        self._max_keys = max_degree - 1
        self._min_keys = (max_degree + 1) // 2 - 1  # ceil(max_degree / 2) - 1
        self._root = _Node()

    def is_empty(self):
        """Return True if the tree holds no keys."""
        return len(self._root.keys) == 0

    @staticmethod
    def _lower_bound(node, key):
        # Index of the first key in the node that is not smaller than key —
        # the key itself if the node holds it, otherwise the gap it falls
        # into.
        i = 0
        while i < len(node.keys) and node.keys[i] < key:
            i += 1
        return i

    def contains(self, key):
        """Return True if the tree holds ``key``."""
        node = self._root
        while True:
            i = self._lower_bound(node, key)
            if i < len(node.keys) and node.keys[i] == key:
                return True
            if node.is_leaf():
                return False
            # Descend through the gap the key falls into.
            node = node.children[i]

    def insert(self, key):
        """Insert ``key``.

        The key goes into the leaf it belongs in; if that leaf now holds
        one key too many it splits, and the split can repeat all the way
        up to the root. Return False if the key was already in the tree.
        """
        # Step 1: walk down to the leaf the key belongs in, remembering
        # the path so the splits can climb back up it.
        path = []
        node = self._root
        while True:
            i = self._lower_bound(node, key)
            if i < len(node.keys) and node.keys[i] == key:
                return False  # already in the tree
            if node.is_leaf():
                # Step 2: the leaf makes room and takes the key.
                node.keys.insert(i, key)
                break
            path.append(node)
            node = node.children[i]

        # Step 3: while a node holds one key too many, split it. Its
        # middle key goes up into the parent, which may overflow in its
        # turn.
        while len(node.keys) > self._max_keys:
            parent = path.pop() if path else None
            self._split(node, parent)
            if parent is None:
                break  # the root split: the tree is one level taller
            node = parent
        return True

    def _split(self, node, parent):
        # Splits an overfull node in two around its middle key, which moves
        # up into the parent. With an even number of keys there are two
        # middles; the right-hand one goes up, leaving the extra key in the
        # left half. A split root grows a new root above it.
        mid = len(node.keys) // 2
        middle_key = node.keys.pop(mid)

        right = _Node()
        while len(node.keys) > mid:
            right.keys.append(node.keys.pop(mid))
        if not node.is_leaf():
            while len(node.children) > mid + 1:
                right.children.append(node.children.pop(mid + 1))

        if parent is None:
            parent = _Node()
            parent.children.append(node)
            self._root = parent
        at = parent.children.index(node)
        parent.keys.insert(at, middle_key)
        parent.children.insert(at + 1, right)

    def delete(self, key):
        """Delete ``key``.

        A key can only leave a leaf, so a key inside an internal node
        first trades places with its successor. Removing it may leave a
        node below the minimum, which is repaired from the bottom up by
        borrowing a key from a neighbour or merging with one. Return False
        if the key was not in the tree.
        """
        # Step 1: walk down to the key, remembering the path so the repair
        # can climb back up it.
        path = []
        node = self._root
        while True:
            index = self._lower_bound(node, key)
            if index < len(node.keys) and node.keys[index] == key:
                break
            if node.is_leaf():
                return False  # not in the tree
            path.append(node)
            node = node.children[index]

        # Step 2: a key inside an internal node trades places with its
        # successor — the leftmost key of the subtree to its right — so
        # that it can leave from a leaf.
        if not node.is_leaf():
            holder = node
            path.append(node)
            node = node.children[index + 1]
            while not node.is_leaf():
                path.append(node)
                node = node.children[0]
            holder.keys[index] = node.keys[0]
            node.keys[0] = key
            index = 0

        # Step 3: the leaf gives the key up. It may now be below the
        # minimum — even empty — and stays that way until Step 4 repairs
        # it.
        node.keys.pop(index)

        # Step 4: repair from the bottom up. A node below the minimum
        # borrows a spare key from a neighbour, through the parent; if
        # neither neighbour has one, it merges with a neighbour and the key
        # that separated them, which takes a key from the parent — so the
        # repair continues one level higher.
        min_keys = self._min_keys
        while node is not self._root and len(node.keys) < min_keys:
            parent = path.pop()
            at = parent.children.index(node)
            left = parent.children[at - 1] if at > 0 else None
            right = (parent.children[at + 1]
                     if at < len(parent.children) - 1 else None)

            if left is not None and len(left.keys) > min_keys:
                self._borrow_from_left(parent, at)
            elif right is not None and len(right.keys) > min_keys:
                self._borrow_from_right(parent, at)
            else:
                # Merge with the left neighbour if there is one.
                first = at - 1 if at > 0 else at
                self._merge(parent, first)
                if parent is self._root and len(parent.keys) == 0:
                    # The tree is one level shorter.
                    self._root = parent.children[0]
                    break
            node = parent
        return True

    @staticmethod
    def _borrow_from_left(parent, at):
        # The separating key comes down from the parent to the front of the
        # child at index at; the left neighbour's last key goes up to
        # replace it.
        node = parent.children[at]
        left = parent.children[at - 1]
        node.keys.insert(0, parent.keys[at - 1])
        parent.keys[at - 1] = left.keys.pop()
        if not left.is_leaf():
            node.children.insert(0, left.children.pop())

    @staticmethod
    def _borrow_from_right(parent, at):
        # The separating key comes down from the parent to the end of the
        # child at index at; the right neighbour's first key goes up to
        # replace it.
        node = parent.children[at]
        right = parent.children[at + 1]
        node.keys.append(parent.keys[at])
        parent.keys[at] = right.keys.pop(0)
        if not right.is_leaf():
            node.children.append(right.children.pop(0))

    @staticmethod
    def _merge(parent, first):
        # Merges the child at index first + 1 into the child at index
        # first, with the key that separated them in between.
        left = parent.children[first]
        right = parent.children[first + 1]
        left.keys.append(parent.keys.pop(first))
        left.keys.extend(right.keys)
        left.children.extend(right.children)
        parent.children.pop(first + 1)
