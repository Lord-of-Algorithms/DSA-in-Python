def heap_sort_iterative(array):
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
    while i < size // 2:  # Only non-leaf nodes need to be heapified
        largest_child_index = get_largest_child_index(array, i, size)
        if examined >= array[largest_child_index]:
            break  # The heap property is satisfied
        # Overwrite the current node with the value of its largest child
        array[i] = array[largest_child_index]
        # Move the index to the largest child to continue the process down the tree
        i = largest_child_index
    # Place the original root value at the final position determined by the last iteration
    array[i] = examined


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
