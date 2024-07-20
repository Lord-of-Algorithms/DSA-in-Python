class LinkedList:
    """
    Represents a singly linked list.
    """

    class Node:
        """
        Represents a node in a linked list. Each node contains data and a reference to the next node.
        """

        def __init__(self, data):
            """
            Initializes a new node with the specified data and sets the next node reference to None.
            """
            self.data = data
            self.next = None

    def __init__(self):
        """
        Initializes an empty linked list.
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
        node = self.Node(value)
        node.next = self.head
        self.head = node

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
            raise ValueError(f"Predecessor value {pred_value} not found in the list")
        node = self.Node(value)
        node.next = pred.next
        pred.next = node

    def insert_last(self, value):
        """
        Inserts a new node with the specified value at the end of the list.
        """
        if self.is_empty():
            self.head = self.Node(value)
            return
        pred = self.head
        while pred.next is not None:
            pred = pred.next
        pred.next = self.Node(value)

    def delete_first(self):
        """
        Deletes and returns the first node from the list. If the list is empty, returns None.
        """
        if self.is_empty():
            return None
        temp = self.head
        self.head = self.head.next
        return temp

    def delete_by_value(self, value):
        """
        Deletes and returns the first found node containing the specified value.
        If no such node exists, does nothing and returns None.
        """
        if self.is_empty():
            return None
        if self.head.data == value:
            # Delete the head
            temp = self.head
            self.head = self.head.next
            return temp
        pred = self.head
        temp = self.head.next
        while temp is not None and temp.data != value:
            pred = pred.next
            temp = temp.next
        if temp is not None:
            # The node to be deleted is found.
            # Delete it by changing references.
            pred.next = temp.next
        return temp

    def delete_last(self):
        """
        Deletes and returns the last node from the list.
        If the list is empty, returns None.
        """
        if self.is_empty():
            return None
        if self.head.next is None:
            # There is only one node
            temp = self.head
            self.head = None
            return temp
        pred = self.head
        temp = self.head.next
        while temp.next is not None:
            pred = pred.next
            temp = temp.next
        pred.next = None
        return temp
