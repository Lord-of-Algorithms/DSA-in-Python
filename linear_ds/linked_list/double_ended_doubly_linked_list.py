class DoubleEndedDoublyLinkedList:
    """
    Represents a doubly linked list with references to both the head and tail.

    Each node links to both its next and its previous node, so the list can be
    traversed in either direction and a node's neighbours can be re-linked
    directly. Keeping a tail reference makes insertion and deletion at the end
    O(1), just like at the beginning - and unlike a singly double-ended list,
    even deletion at the end is O(1), because the last node knows its own
    predecessor through its prev reference.
    """

    class Node:
        """
        Represents a node in a doubly linked list. Each node holds data and
        references to both the next and the previous node.
        """

        def __init__(self, data):
            """
            Initializes a new node with the specified data and unset links.
            """
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        """
        Initializes an empty list with no head or tail.
        """
        self.head = None
        self.tail = None

    def is_empty(self):
        """
        Checks if the linked list is empty.

        :return: True if the list is empty, False otherwise.
        """
        return self.head is None

    def insert_first(self, value):
        """
        Inserts a new node with the specified value at the start of the list.
        """
        new_node = self.Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            # Link the new node and the old first node to each other
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_after(self, pred_value, value):
        """
        Inserts a new node with the specified value immediately after the node
        that has the specified predecessor value.

        :param pred_value: The value after which the new node should be inserted.
        :param value: The value to insert in the new node.
        :raises ValueError: If the predecessor node with pred_value is not found.
        """
        pred = self.head
        while pred is not None and pred.data != pred_value:
            pred = pred.next
        if pred is None:
            raise ValueError(f"Predecessor value {pred_value} not found in the list.")
        new_node = self.Node(value)
        # Link the new node to both of its neighbours
        new_node.next = pred.next
        new_node.prev = pred
        if pred.next is not None:
            pred.next.prev = new_node
        else:
            # Inserting after the last node: the new node becomes the tail
            self.tail = new_node
        pred.next = new_node

    def insert_last(self, value):
        """
        Inserts a new node with the specified value at the end of the list.
        The tail reference makes this O(1) - no walk needed.
        """
        new_node = self.Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            # Link the new node back to the current last node,
            # then move the tail forward onto it
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete_first(self):
        """
        Deletes the first node from the list.
        """
        if self.is_empty():
            raise Exception("The list is empty.")
        if self.head == self.tail:
            # There is only one node
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_by_value(self, value):
        """
        Deletes the first occurrence of a node with the specified value.
        """
        if self.is_empty():
            raise Exception("The list is empty.")
        cur = self.head
        while cur is not None and cur.data != value:
            cur = cur.next
        if cur is None:
            raise ValueError(f"Value {value} not found in the list.")
        if cur == self.head:
            self.delete_first()
        elif cur == self.tail:
            self.delete_last()
        else:
            # A node in the middle: re-link its two neighbours to each other
            cur.prev.next = cur.next
            cur.next.prev = cur.prev

    def delete_last(self):
        """
        Deletes the last node from the list.
        The tail reference makes this O(1) - the last node's predecessor is just
        tail.prev, so no walk is needed.
        """
        if self.is_empty():
            raise Exception("The list is empty.")
        if self.head == self.tail:
            # There is only one node
            self.head = None
            self.tail = None
        else:
            # The last node knows its own predecessor, so step the tail
            # straight back to it and clear its forward link
            self.tail = self.tail.prev
            self.tail.next = None
