def quick_sort_lomuto(array, low, high):
    """
    Public function to start the Quick Sort process using the Lomuto partition scheme.

    :param array: The array to be sorted.
    :param low: The starting index of the segment of the array to be sorted.
    :param high: The ending index of the segment of the array to be sorted.
    """
    if low < high:
        # Partition the array around the pivot
        pivot_index = partition(array, low, high)

        # Recursively sort the sub-array before the pivot
        quick_sort_lomuto(array, low, pivot_index - 1)
        # Recursively sort the sub-array after the pivot
        quick_sort_lomuto(array, pivot_index + 1, high)


def partition(array, low, high):
    """
    Partitions the array using the Lomuto partition scheme and returns the index of the pivot.
    The last element is chosen as the pivot.

    :param array: The array to be partitioned.
    :param low: The starting index for the partitioning.
    :param high: The ending index for the partitioning.
    :return: The index of the pivot element after partitioning.
    """
    pivot = array[high]
    i = low  # Index of smaller element

    for j in range(low, high):
        # If current element is smaller than the pivot
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]  # Swap
            i += 1

    array[i], array[high] = array[high], array[i]  # Swap pivot into its correct position
    return i  # Return the partitioning index
