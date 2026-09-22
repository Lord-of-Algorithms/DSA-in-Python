"""
Demonstrates BTree: search, insertion — including a split that adds a
level — and deletion with each of the repairs it can need. The trees are
the worked examples from the app's B-tree topic, all of maximum degree 4.
"""

from btree.b_tree import BTree
from btree.b_tree_printer import BTreePrinter


def build_tree(first, last, step):
    """A tree of maximum degree 4 holding first, first + step, ..., last,
    inserted in ascending order."""
    tree = BTree(4)
    for key in range(first, last + 1, step):
        tree.insert(key)
    return tree


def demonstrate_insert():
    """Keys 10, 15, ..., 65 fill both the root and the leaf where 70
    belongs. Inserting 70 overflows that leaf, which splits and sends 65
    up; the root overflows in its turn and splits too, and the tree grows
    a level.
    """
    print('=== Insert ===')
    tree = build_tree(10, 65, 5)
    print('After inserting 10, 15, ..., 65:')
    BTreePrinter.print_tree(tree)
    print('contains(45) = {}, contains(47) = {}'.format(
        tree.contains(45), tree.contains(47)))

    tree.insert(70)
    print('\nInsert 70 — the leaf splits, then the root: one level more.')
    BTreePrinter.print_tree(tree)


def demonstrate_delete():
    """Three deletions, one for each way a delete can end:

      * a leaf left below the minimum borrows from its neighbour;
      * two merges, one above the other, empty the root and the tree loses
        a level;
      * a key in an internal node trades places with its successor and
        leaves from a leaf.
    """
    print('\n=== Delete: borrowing from a neighbour ===')
    tree = build_tree(10, 70, 10)
    BTreePrinter.print_tree(tree)
    tree.delete(70)
    print('Delete 70 — its leaf empties and borrows through the parent:')
    BTreePrinter.print_tree(tree)

    print('\n=== Delete: a merge that removes a level ===')
    tree = build_tree(10, 70, 5)
    for key in range(70, 54, -5):
        tree.delete(key)
    BTreePrinter.print_tree(tree)
    tree.delete(40)
    print('Delete 40 — two merges empty the root: one level less.')
    BTreePrinter.print_tree(tree)

    print('\n=== Delete: a key in an internal node ===')
    tree = build_tree(10, 80, 10)
    BTreePrinter.print_tree(tree)
    tree.delete(60)
    print('Delete 60 — it trades places with its successor 70 and leaves '
          'from a leaf:')
    BTreePrinter.print_tree(tree)


if __name__ == '__main__':
    demonstrate_insert()
    demonstrate_delete()
