from enum import Enum

from sorting.heap.heap_sort_iterative import heap_sort_iterative
from sorting.heap.heap_sort_recursive import heap_sort_recursive


class SortNature(Enum):
    """
    Defines the nature of the sorting method to be used in the Heap Sort.
    It supports both iterative and recursive approaches.
    """
    Iterative = 1
    Recursive = 2


def heap_sort(array, sort_nature):
    """
    Sorts an array using either an iterative or recursive heap sort approach

    :param array: The array (list) to be sorted.
    :param sort_nature: The type of sorting method to use, either Iterative or Recursive.
    :raises ValueError: If an unsupported sort nature is provided.
    """
    if array is None or len(array) <= 1:
        return  # No need to sort if the array is None, empty, or has one element.

    if sort_nature == SortNature.Iterative:
        heap_sort_iterative(array)
    elif sort_nature == SortNature.Recursive:
        heap_sort_recursive(array)
    else:
        raise ValueError("Unsupported sort nature provided.")


def demo_heap_sort():
    """Demonstrates the usage of the Heap Sort function."""
    array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", array)

    heap_sort(array, SortNature.Iterative)

    print("Sorted array:", array)


if __name__ == "__main__":
    demo_heap_sort()
