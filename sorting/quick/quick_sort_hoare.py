def quick_sort_hoare(array, low, high):
    """
    Public function to start the Quick Sort process using the Hoare partition scheme.

    :param array: The array to be sorted.
    :param low: The starting index of the segment of the array to be sorted.
    :param high: The ending index of the segment of the array to be sorted.
    """
    if low < high:
        # Partition the array and obtain the index that divides the partitions
        partition_index = partition(array, low, high)

        # Unlike Lomuto's partition, Hoare's partition
        # might not place the pivot in its final position.
        # Therefore, both recursive calls need to handle segments
        # that potentially include the pivot.
        quick_sort_hoare(array, low, partition_index)
        quick_sort_hoare(array, partition_index + 1, high)


def partition(array, low, high):
    """
    Partitions the array using the Hoare partition scheme and returns the index that divides the partitions.

    :param array: The array to be partitioned.
    :param low: The starting index for the partitioning.
    :param high: The ending index for the partitioning.
    :return: The partition index, which is the last index in the lower partition. This index is not necessarily the final position of the pivot.
    """
    pivot = array[low]  # Pivot chosen as the first element
    i = low - 1
    j = high + 1

    while True:
        # Move right while item is less than pivot
        i += 1
        while array[i] < pivot:
            i += 1

        # Move left while item is greater than pivot
        j -= 1
        while array[j] > pivot:
            j -= 1

        if i >= j:
            return j  # j is the last index in the lower partition

        # Swap elements at i and j
        array[i], array[j] = array[j], array[i]
