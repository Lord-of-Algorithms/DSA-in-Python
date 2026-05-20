"""
Demonstrates Trie operations: insert, search, delete (with cleanup of
empty branches), and autocomplete (starts_with) on a small pool of
words. Output is annotated so the trace reads as a tour of the four
operations.
"""

from trie import Trie


def demo_trie():
    trie = Trie()

    print('=== Insert ===')
    # Intentionally NOT alphabetical so the output below reflects the
    # dict insertion-order child iteration: children of each node are
    # visited in the order they were first added (Python 3.7+ dict
    # preserves insertion order). See TrieNode docstring for the
    # alternative "sort at iteration" approach.
    for word in ['topology', 'cat', 'cap', 'cabin',
                 'catfish', 'cab', 'top', 'catch']:
        trie.insert(word)
        print(f'insert("{word}")   size={trie.size()}')

    print('\n=== Words ===')
    # Note: NOT alphabetical. Words come out in the order DFS visits their
    # end-of-word nodes, and the per-node child order follows the insertion
    # sequence above (cat went in before cap, so 't' is the first child of
    # 'a', etc.).
    print(trie.words())

    print('\n=== Search ===')
    for word in ['cab', 'cat', 'catch', 'ca', 'catfishy', 'topology']:
        print(f'search("{word}") -> {trie.search(word)}')
    # Note: search("ca") is False because "ca" is only a prefix here, not
    # a stored word. The end-of-word flag is the distinction.

    print('\n=== StartsWith (autocomplete) ===')
    for prefix in ['c', 'ca', 'cat', 'to', 'xy']:
        print(f'starts_with("{prefix}") -> {trie.starts_with(prefix)}')
    # "xy" diverges immediately -> empty list.

    print('\n=== Delete ===')
    # Delete a word whose path is shared by longer words.
    # -> Unmark the end-of-word flag on its terminal node, but DON'T
    #    remove any nodes -- the path stays because there are children
    #    below it.
    # "cat" sits at the 't' node under c-a; 't' has children 'f' (catfish)
    # and 'c' (catch), so cleanup is a no-op.
    print(f'delete("cat")   -> {trie.delete("cat")}')
    print(f'words() -> {trie.words()}')
    print(f'search("cat")     -> {trie.search("cat")}')
    print(f'search("catch")   -> {trie.search("catch")}')
    print(f'search("catfish") -> {trie.search("catfish")}')

    # Delete a word whose tail is unique -- cleanup DOES remove nodes.
    # "catch" is c-a-t-c-h. After unmarking 'h', the cleanup walk runs:
    #   * h: not end-of-word, no children -> remove.
    #   * c (under c-a-t): not end-of-word, no children (h was just
    #     removed) -> remove.
    #   * t (under c-a): not end-of-word, but has child 'f' (for catfish)
    #     -> STOP. The catfish path stays intact.
    print(f'delete("catch") -> {trie.delete("catch")}')
    print(f'words() -> {trie.words()}')

    # Try to delete something that isn't there.
    print(f'delete("xyz")   -> {trie.delete("xyz")}')

    print('\n=== Final state ===')
    print(f'size={trie.size()}, words={trie.words()}')


if __name__ == '__main__':
    demo_trie()
