class DoubleEndedLinkedList:
    """
    Implements a singly linked list with references to both the head and tail,
    allowing efficient insertions at both ends of the list.
    """

    class Node:
        """
        Represents a node in a linked list.
        """

        def __init__(self, data):
            """
            Initializes a new node with the specified data.
            """
            self.data = data
            self.next = None

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
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, pred_value, value):
        """
        Inserts a new node with the specified value immediately after the node that has the specified predecessor value.

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
        new_node.next = pred.next
        pred.next = new_node
        if pred == self.tail:
            self.tail = new_node

    def insert_last(self, value):
        """
        Inserts a new node with the specified value at the end of the list.
        """
        new_node = self.Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            # Update the tail's next reference
            # and the tail reference
            self.tail.next = new_node
            self.tail = new_node

    def delete_first(self):
        """
        Deletes the first node from the list.
        """
        if self.is_empty():
            raise Exception("The list is empty.")

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

    def delete_by_value(self, value):
        """
        Deletes the first occurrence of a node with
        the specified value.
        """
        if self.is_empty():
            raise Exception("The list is empty.")

        if self.head.data == value:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            return

        pred = self.head
        temp = self.head.next
        while temp is not None and temp.data != value:
            pred = pred.next
            temp = temp.next

        if temp is not None:
            pred.next = temp.next
            if pred.next is None:
                self.tail = pred
        else:
            raise ValueError(f"Value {value} not found in the list.")

    def delete_last(self):
        """
        Deletes the last node from the list.
        """
        if self.is_empty():
            raise Exception("The list is empty.")

        # If there's only one node in the list
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            # Find the second last node in the list
            pred = self.head
            while pred.next != self.tail:
                pred = pred.next
            # Update the second last node's next
            # reference and the tail reference
            pred.next = None
            self.tail = pred
