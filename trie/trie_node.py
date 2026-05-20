class TrieNode:
    """
    One node of a Trie. Each node holds a single character and a dict of its
    children (one child per outgoing character). A node also carries a flag
    indicating whether the path from the root to this node spells a stored
    word — without that flag the trie could not tell "cat" (a stored word)
    from "cat" appearing only as a prefix of "catch".

    The root node is created with the sentinel character '\\0' and is never
    a stored word itself. Every other node holds the character that its
    incoming edge corresponds to.

    Children iteration order:

    self.children is a plain dict. In Python 3.7+ dicts preserve insertion
    order, so iterating self.children.items() yields children in the order
    they were first added — useful for stable output in Trie.words() and
    Trie.starts_with(). If you want alphabetical iteration instead, sort at
    iteration time inside Trie._collect_words (the only place that walks
    children for output — insert/search/delete use children.get(c) lookups
    and don't care about order):

        for c, child in sorted(node.children.items()):
            path.append(c)
            self._collect_words(child, path, out)
            path.pop()

    The cost is O(k log k) per iteration where k is the number of children
    at the node (small in practice — bounded by alphabet size, ≤ 26 for
    English letters). Lookups (self.children[c]) stay O(1) regardless.
    """

    def __init__(self, character, parent):
        """
        :param character: The character this node holds. '\\0' for the root sentinel.
        :param parent:    Parent in the trie. None for the root.
        """
        self.character = character
        self.parent = parent
        self.is_end_of_word = False
        self.children = {}

    def is_root(self):
        """
        :return: True iff this is the root sentinel (no parent, no character).
        """
        return self.parent is None
