from linear_ds.queue.bounded_array_qeueue import BoundedArrayQueue
from linear_ds.queue.dynamic_array_queue import DynamicArrayQueue
from linear_ds.queue.linked_list_queue import LinkedListQueue


def demo_bounded_array_queue():
    print("Demo: BoundedArrayQueue")
    queue = BoundedArrayQueue(3)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print(f"Dequeue: {queue.dequeue()}")  # Expected Output: 1
    print(f"Peek Front: {queue.peek()}")  # Expected Output: 2
    print(f"Is empty: {queue.is_empty()}")  # Expected Output: False

    queue.dequeue()
    queue.dequeue()
    print(f"Is empty after dequeuing all elements: {queue.is_empty()}")  # Expected Output: True


def demo_dynamic_array_queue():
    print("\nDemo: DynamicArrayQueue")
    queue = DynamicArrayQueue(2)
    queue.enqueue('apple')
    queue.enqueue('banana')
    queue.enqueue('cherry')

    print(f"Dequeue: {queue.dequeue()}")  # Expected Output: 'apple'
    print(f"Peek Front: {queue.peek()}")  # Expected Output: 'banana'
    print(f"Is empty: {queue.is_empty()}")  # Expected Output: False

    queue.dequeue()
    queue.dequeue()
    print(f"Is empty after dequeuing all elements: {queue.is_empty()}")  # Expected Output: True


def demo_linked_list_queue():
    print("\nDemo: LinkedListQueue")
    queue = LinkedListQueue()
    queue.enqueue(100)
    queue.enqueue(200)

    print(f"Dequeue: {queue.dequeue()}")  # Expected Output: 100
    print(f"Peek Front: {queue.peek()}")  # Expected Output: 200
    print(f"Is empty: {queue.is_empty()}")  # Expected Output: False

    queue.dequeue()
    print(f"Is empty after dequeuing all elements: {queue.is_empty()}")  # Expected Output: True


if __name__ == "__main__":
    demo_bounded_array_queue()
    demo_dynamic_array_queue()
    demo_linked_list_queue()
