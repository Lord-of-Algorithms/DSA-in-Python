"""
Demonstrates MinHeap operations: insert, peek_min, extract_min (which
yields the values in ascending order), and delete.
"""

from heap.min_heap import MinHeap


def demo_min_heap():
    heap = MinHeap(15)

    print('=== Insert ===')
    for value in [5, 3, 8, 1, 9, 2, 7]:
        heap.insert(value)
        print('insert({})   min={}   size={}'.format(
            value, heap.peek_min(), heap.size()))

    print('\n=== Delete ===')
    # Delete the node at index 2 to show the replacement being sifted.
    print('delete(index 2)')
    heap.delete(2)
    print('min={}   size={}'.format(heap.peek_min(), heap.size()))

    print('\n=== Extract-min (ascending) ===')
    values = []
    while not heap.is_empty():
        values.append(heap.extract_min())
    print(', '.join(str(value) for value in values))


if __name__ == '__main__':
    demo_min_heap()
