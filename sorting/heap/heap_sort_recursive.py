def heap_sort_recursive(array):
    """
    Sorts an array using the Heap Sort algorithm.

    :param array: The array to be sorted.
    """
    n = len(array)
    # Build a max heap from the array
    build_heap(array, n)
    for i in range(n - 1, 0, -1):
        # Swap the root of the heap with the last element of the unsorted part
        array[0], array[i] = array[i], array[0]
        # Heapify the root element to maintain the heap property
        heapify(array, 0, i)


def build_heap(array, size):
    """
    Transforms an array into a max heap.

    :param array: The array to transform into a heap.
    :param size: The number of elements in the array.
    """
    for i in range(size // 2 - 1, -1, -1):
        heapify(array, i, size)


def heapify(array, i, size):
    """
    Ensures the heap property for a subtree rooted at the index i.

    :param array: The heap array.
    :param i: The root index of the subtree.
    :param size: The size of the heap (or subheap during sorting).
    """
    examined = array[i]
    largest_child_index = get_largest_child_index(array, i, size)
    if largest_child_index < size and examined < array[largest_child_index]:
        # Perform the swap
        array[i], array[largest_child_index] = array[largest_child_index], array[i]
        # Recursively heapify the affected subtree
        heapify(array, largest_child_index, size)


def get_largest_child_index(array, i, size):
    """
    Returns the index of the largest child of a given node.

    :param i: The index of the node.
    :param array: The heap array.
    :param size: The size of the heap.
    :return: The index of the largest child.
    """
    left = 2 * i + 1
    right = left + 1
    if right < size and array[left] < array[right]:
        return right  # Right child is larger
    return left  # Left child is larger or only child
