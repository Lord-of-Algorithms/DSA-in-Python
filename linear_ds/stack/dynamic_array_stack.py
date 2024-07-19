from linear_ds.stack.stack import Stack


class DynamicArrayStack(Stack):
    """
    A stack implementation using a dynamic array (Python list), allowing it to grow
    as needed.
    """

    def __init__(self):
        """
        Initializes the empty stack.
        """
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty.")
        return self.data.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty.")
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0
