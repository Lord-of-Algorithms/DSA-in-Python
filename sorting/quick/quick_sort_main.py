from enum import Enum

from sorting.quick.quick_sort_hoare import quick_sort_hoare
from sorting.quick.quick_sort_lomuto import quick_sort_lomuto


class PartitionScheme(Enum):
    """
    Defines the types of partition schemes that can be used for Quick Sort.
    """
    Lomuto = 1
    Hoare = 2


def quick_sort(array, partition_scheme):
    """
    Sorts an array using the specified partition scheme for Quick Sort.

    :param array: The array (list) to be sorted.
    :param partition_scheme: The partition scheme to use for sorting: Lomuto or Hoare.
    :raises ValueError: If an unsupported partition scheme is provided.
    """
    if array is None or len(array) <= 1:
        return  # No need to sort if the array is None, empty, or has one element.

    if partition_scheme == PartitionScheme.Lomuto:
        quick_sort_lomuto(array, 0, len(array) - 1)
    elif partition_scheme == PartitionScheme.Hoare:
        quick_sort_hoare(array, 0, len(array) - 1)
    else:
        raise ValueError(f"Unsupported partition scheme: {partition_scheme}")


def demo_quick_sort():
    """Demonstrates the usage of the Quick Sort function."""
    array = ["3", 34, 25, 12, 22, 11, 90]
    print("Original array:", array)

    quick_sort(array, PartitionScheme.Lomuto)

    print("Sorted array:", array)


if __name__ == "__main__":
    demo_quick_sort()
