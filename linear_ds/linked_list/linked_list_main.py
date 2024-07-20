from linear_ds.linked_list.double_ended_linked_list import DoubleEndedLinkedList
from linear_ds.linked_list.linked_list import LinkedList


def print_list(node):
    """
    Helper function to print the elements of the list from the given node.
    """
    elements = []
    while node:
        elements.append(str(node.data))
        node = node.next
    print(" -> ".join(elements))


def demo_linked_list():
    print("Demo: LinkedList")
    ll = LinkedList()
    ll.insert_first(10)
    ll.insert_first(20)
    ll.insert_last(5)
    ll.insert_after(10, 15)

    print("Current List:")
    print_list(ll.head)

    print("Deleting first:")
    ll.delete_first()
    print_list(ll.head)

    print("Deleting by value (15):")
    ll.delete_by_value(15)
    print_list(ll.head)


def demo_double_ended_linked_list():
    print("\nDemo: DoubleEndedLinkedList")
    dll = DoubleEndedLinkedList()
    dll.insert_first("apple")
    dll.insert_last("banana")
    dll.insert_first("cherry")
    dll.insert_last("mango")

    print("Current List:")
    print_list(dll.head)

    print("Deleting first:")
    dll.delete_first()
    print_list(dll.head)

    print("Deleting last:")
    dll.delete_last()
    print_list(dll.head)

    print("Inserting after (apple):")
    dll.insert_after("apple", "apricot")
    print_list(dll.head)


if __name__ == "__main__":
    demo_linked_list()
    demo_double_ended_linked_list()
