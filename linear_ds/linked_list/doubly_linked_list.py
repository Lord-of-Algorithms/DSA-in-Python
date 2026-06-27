class DoublyLinkedList:
    """
    Represents a doubly linked list with a reference to the head only.

    Each node links to both its next and its previous node, so the list can be
    traversed in either direction and a node's neighbours can be re-linked
    directly. Without a tail reference, reaching the last node means walking from
    the head, so insertion and deletion at the end are O(n).
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
        Initializes an empty doubly linked list.
        """
        self.head = None

    def is_empty(self):
        """
        Checks if the linked list is empty.

        :return: True if the list is empty, False otherwise.
        """
        return self.head is None

    def insert_first(self, value):
        """
        Inserts a new node with the specified value at the beginning of the list.
        """
        new_node = self.Node(value)
        if not self.is_empty():
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
        pred.next = new_node

    def insert_last(self, value):
        """
        Inserts a new node with the specified value at the end of the list.
        With only a head reference, this walks from the head to the last node.
        """
        new_node = self.Node(value)
        if self.is_empty():
            self.head = new_node
            return
        pred = self.head
        while pred.next is not None:
            pred = pred.next
        new_node.prev = pred
        pred.next = new_node

    def delete_first(self):
        """
        Deletes the first node from the list.
        """
        if self.is_empty():
            raise Exception("The list is empty.")
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None

    def delete_by_value(self, value):
        """
        Deletes the first found node containing the specified value.
        """
        if self.is_empty():
            raise Exception("The list is empty.")
        cur = self.head
        while cur is not None and cur.data != value:
            cur = cur.next
        if cur is None:
            raise ValueError(f"Value {value} not found in the list.")
        if cur is self.head:
            self.delete_first()
        else:
            # Re-link the predecessor over the doomed node...
            cur.prev.next = cur.next
            if cur.next is not None:
                # ...and the successor back, unless this was the last node
                cur.next.prev = cur.prev

    def delete_last(self):
        """
        Deletes the last node from the list.
        With only a head reference, this walks from the head to the last node.
        """
        if self.is_empty():
            raise Exception("The list is empty.")
        if self.head.next is None:
            # There is only one node
            self.head = None
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        # The last node knows its own predecessor, so step straight back to it
        cur = cur.prev
        cur.next = None
