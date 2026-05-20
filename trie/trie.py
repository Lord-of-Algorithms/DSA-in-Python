from trie_node import TrieNode


class Trie:
    """
    A trie (pronounced "try"): a tree-shaped data structure where each node
    holds a single character, and a stored word corresponds to a path from
    the root to a node flagged as end-of-word.

    Why a trie? Two operations a trie does extremely well that a set or
    balanced BST cannot:

      * Prefix lookup — "give me every word that starts with 'ca'" runs in
        O(L + K) where L is the prefix length and K is the number of
        matches. A set would have to scan every entry.

      * Ordered enumeration — depth-first traversal returns words in a
        deterministic order determined by each node's children dict. This
        implementation uses a plain dict (insertion order on Python 3.7+);
        iterate sorted(node.children.items()) instead if you need
        alphabetical output (see TrieNode).

    Complexity:

        L = length of the word / prefix
        N = total words stored
        K = matches under a given prefix

        insert       O(L)
        delete       O(L)
        search       O(L)
        starts_with  O(L + K)
        space        O(N * L) worst case; much less when prefixes overlap

    Used in: autocomplete keyboards, spell-check and "did-you-mean?",
    T9 / predictive text, IP-routing longest-prefix match, DNS lookups.
    """

    def __init__(self):
        """
        Create an empty trie. The root sentinel holds no character; every
        word path begins at the root and takes its first character from
        one of the root's children.
        """
        self.root = TrieNode('\0', None)
        self._word_count = 0

    def is_empty(self):
        """
        :return: True iff no words are stored.
        """
        return self._word_count == 0

    def size(self):
        """
        :return: Total number of stored words.
        """
        return self._word_count

    def clear(self):
        """
        Remove every word.
        """
        self.root.children.clear()
        self._word_count = 0

    def insert(self, word):
        """
        Insert ``word`` into the trie. No-op if the word is already present.
        None or empty words are ignored.

        :param word: The word to insert.
        """
        if not word:
            return
        node = self.root
        for c in word:
            # If the child for this character is missing, create it.
            # Shared prefixes share nodes — this is the heart of the trie's
            # memory advantage.
            child = node.children.get(c)
            if child is None:
                child = TrieNode(c, node)
                node.children[c] = child
            node = child
        # Mark the final node as end-of-word. Only bump the word count if
        # we transitioned the flag from False to True — re-inserting an
        # existing word is a no-op.
        if not node.is_end_of_word:
            node.is_end_of_word = True
            self._word_count += 1

    def search(self, word):
        """
        Check whether ``word`` is stored in the trie. "Stored" means the
        path exists AND the final node is flagged end-of-word.
        ``search("cat")`` returns False if only ``"catch"`` is stored, even
        though the "cat" path is reachable as a prefix.

        :param word: The word to search for.
        :return: True iff the word is a stored word.
        """
        if not word:
            return False
        node = self._find_terminal_node(word)
        return node is not None and node.is_end_of_word

    def delete(self, word):
        """
        Delete ``word`` from the trie and remove any nodes that became
        orphaned (no longer end-of-word and no remaining children).

        The cleanup phase runs after the end-of-word flag is cleared: walk
        back up from the deleted leaf and remove every node that has no
        end-of-word flag AND no children. Stop at the first node that's
        still part of another word's path — either it carries its own
        end-of-word flag, or it has another child branching off. Deleting
        ``"cab"`` from a trie that also stores ``"cat"`` removes only the
        ``'b'`` node; the shared ``"c-a"`` path stays because ``'a'`` still
        has its ``'t'`` child.

        :param word: The word to delete.
        :return: True if a word was actually removed, False if the word was
                 never in the trie.
        """
        if not word:
            return False
        node = self._find_terminal_node(word)
        if node is None or not node.is_end_of_word:
            return False

        node.is_end_of_word = False
        self._word_count -= 1

        # Cleanup walk: remove the deleted leaf and its empty ancestors
        # until we hit a node that's still useful.
        while not node.is_root() and not node.is_end_of_word and not node.children:
            parent = node.parent
            del parent.children[node.character]
            node = parent
        return True

    def starts_with(self, prefix):
        """
        Return every word stored in the trie that begins with ``prefix``.
        Returns an empty list if the prefix can't be walked (a non-existent
        prefix means no matches by definition).

        An empty or None prefix matches every word.

        Algorithm: descend along the prefix to find its terminal node, then
        DFS the subtree rooted there to collect every end-of-word
        descendant. Each descendant uniquely identifies one stored word —
        the word string is the path from root to that descendant.

        :param prefix: The prefix to search for.
        :return: List of matching words.
        """
        matches = []
        if not prefix:
            prefix_node = self.root
            prefix = ''
        else:
            prefix_node = self._find_terminal_node(prefix)
        if prefix_node is None:
            return matches

        path = [prefix]
        self._collect_words(prefix_node, path, matches)
        return matches

    def words(self):
        """
        Return every word stored in the trie, in insertion-preserving order
        of the underlying dicts. Useful for tests and debugging.

        :return: List of all stored words.
        """
        return self.starts_with('')

    # ---- internals ----

    def _find_terminal_node(self, path):
        """
        Walk the trie following ``path`` character-by-character and return
        the terminal node, or None if any character has no corresponding
        child along the way.

        :param path: The character sequence to walk.
        :return: The terminal node, or None if the path doesn't exist.
        """
        node = self.root
        for c in path:
            child = node.children.get(c)
            if child is None:
                return None
            node = child
        return node

    def _collect_words(self, node, path, out):
        """
        DFS helper for ``starts_with`` and ``words``. Appends node.character
        to ``path`` on the way down, snapshots ''.join(path) into ``out``
        whenever the current node is end-of-word, recurses into every
        child, and pops the appended character on the way back up to leave
        ``path`` untouched for the caller's next branch.

        :param node: The current node to visit.
        :param path: List of strings accumulated so far on the way down
                     (joined with ''.join(...) at end-of-word nodes).
                     Used as a mutable list-buffer to avoid allocating a
                     fresh string per node.
        :param out:  Output list of collected words.
        """
        if node.is_end_of_word:
            out.append(''.join(path))
        for c, child in node.children.items():
            path.append(c)
            self._collect_words(child, path, out)
            path.pop()
