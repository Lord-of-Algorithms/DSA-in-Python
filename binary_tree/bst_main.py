from binary_tree.binary_tree_printer import BinaryTreePrinter
from binary_tree.bst.avl.avl_tree import AvlTree
from binary_tree.bst.red_black.red_black_tree import RedBlackTree
from binary_tree.bst.standard.binary_search_tree_iterative import BinarySearchTreeIterative
from binary_tree.bst.standard.binary_search_tree_recursive import BinarySearchTreeRecursive

from enum import Enum

from binary_tree.traversal.breadth_first_traversal import BreadthFirstTraversal
from binary_tree.traversal.in_order_traversal import InOrderTraversal
from binary_tree.traversal.post_order_traversal import PostOrderTraversal
from binary_tree.traversal.pre_order_traversal import PreOrderTraversal
from binary_tree.traversal.traversal_nature import TraversalNature


class BstType(Enum):
    StandardIterative = 1
    StandardRecursive = 2
    Avl = 3
    RedBlack = 4


def create_tree(tree_type):
    if tree_type == BstType.StandardIterative:
        return BinarySearchTreeIterative()
    elif tree_type == BstType.StandardRecursive:
        return BinarySearchTreeRecursive()
    elif tree_type == BstType.Avl:
        return AvlTree()
    elif tree_type == BstType.RedBlack:
        return RedBlackTree()
    else:
        raise ValueError("Unknown BST type: {}".format(tree_type))


def insert_keys_into_tree(tree, keys):
    for key in keys:
        print("Inserting key:", key)
        tree.insert(key)


def delete_keys_from_tree(tree, keys):
    for key in keys:
        print("Delete node with key:", key)
        tree.delete(key)
        BinaryTreePrinter.print_tree(tree.get_root())


def search_keys_in_tree(tree, keys):
    for key in keys:
        print("Search for a node with key:", key)
        print("Is found:", tree.search(key) is not None)


def demonstrate_traversals(tree):
    print("\nPre-order traversal: ")
    traversal = PreOrderTraversal(TraversalNature.Iterative)
    traversal.traverse(tree.get_root())

    print("\nIn-order traversal: ")
    traversal = InOrderTraversal(TraversalNature.Recursive)
    traversal.traverse(tree.get_root())

    print("\nPost-order traversal: ")
    traversal = PostOrderTraversal(TraversalNature.Recursive)
    traversal.traverse(tree.get_root())

    print("\nBreadth-first traversal: ")
    traversal = BreadthFirstTraversal()
    traversal.traverse(tree.get_root())


bst = create_tree(BstType.RedBlack)
insert_keys_into_tree(bst, [20, 7, 9, 2, 40, 22, 70, 70, 25])
BinaryTreePrinter.print_tree(bst.get_root())
delete_keys_from_tree(bst, [20, 40, 2, 7])
search_keys_in_tree(bst, [70, 44])
demonstrate_traversals(bst)
