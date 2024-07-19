from linear_ds.stack.stack import Stack


class BoundedArrayStack(Stack):
    """
    A stack implementation using a pre-allocated array to store elements, with a fixed maximum size.
    This implementation offers O(1) time complexity for push and pop operations under the assumption
    that the stack's capacity is not exceeded.
    """

    def __init__(self, size: int):
        """
        Initializes the stack with a given size.
        """
        if size <= 0:
            raise ValueError("Size must be greater than zero.")
        self.data = [None] * size  # Initialize the stack with None to represent unused slots
        # Index of the top element
        self.top = -1

    def push(self, element):
        if self.is_full():
            raise Exception("Stack is full.")
        # Increment top and add element
        self.top += 1
        self.data[self.top] = element

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty.")
        element = self.data[self.top]
        # Decrement top which causes the
        # element to be removed
        self.top -= 1
        return element

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty.")
        return self.data[self.top]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        """
        Checks if the stack is full.
        """
        return self.top == len(self.data) - 1
