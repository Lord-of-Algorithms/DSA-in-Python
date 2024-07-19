from linear_ds.stack.bounded_array_stack import BoundedArrayStack
from linear_ds.stack.dynamic_array_stack import DynamicArrayStack
from linear_ds.stack.linked_list_stack import LinkedListStack


def demo_bounded_array_stack():
    print("Demo: BoundedArrayStack")
    stack = BoundedArrayStack(3)
    stack.push(3)
    stack.push(5)
    stack.push(1)

    print(f"Pop: {stack.pop()}")  # Expected Output: 1
    print(f"Peek: {stack.peek()}")  # Expected Output: 5
    print(f"Is empty: {stack.is_empty()}")  # Expected Output: False

    stack.pop()
    stack.pop()
    print(f"Is empty after popping all elements: {stack.is_empty()}")  # Expected Output: True


def demo_dynamic_array_stack():
    print("\nDemo: DynamicArrayStack")
    stack = DynamicArrayStack()
    stack.push('a')
    stack.push('b')

    print(f"Pop: {stack.pop()}")  # Expected Output: 'b'
    print(f"Peek: {stack.peek()}")  # Expected Output: 'a'
    print(f"Is empty: {stack.is_empty()}")  # Expected Output: False

    stack.pop()
    print(f"Is empty after popping all elements: {stack.is_empty()}")  # Expected Output: True


def demo_linked_list_stack():
    print("\nDemo: LinkedListStack")
    stack = LinkedListStack()
    stack.push(10)
    stack.push(20)

    print(f"Pop: {stack.pop()}")  # Expected Output: 20
    print(f"Peek: {stack.peek()}")  # Expected Output: 10
    print(f"Is empty: {stack.is_empty()}")  # Expected Output: False

    stack.pop()
    print(f"Is empty after popping all elements: {stack.is_empty()}")  # Expected Output: True


if __name__ == "__main__":
    demo_bounded_array_stack()
    demo_dynamic_array_stack()
    demo_linked_list_stack()
