from linear_ds.stack.stack import Stack


class LinkedListStack(Stack):
    """
    A stack implementation using a singly linked list.
    """

    class Node:
        """
        Node represents an element in the stack, containing
        a value and reference to the next Node.
        """

        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        """
        Initializes the empty stack.
        """
        # Top element
        self.top = None

    def push(self, element):
        # Create a new node
        node = self.Node(element)
        # Make the new node the top element
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty.")
        element = self.top.data
        # Remove the top element
        self.top = self.top.next
        return element

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty.")
        return self.top.data

    def is_empty(self):
        return self.top is None
