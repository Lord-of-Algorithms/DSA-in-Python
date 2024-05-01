def merge_sort(array):
    """
    Sorts the provided array using the Merge Sort algorithm.

    :param array: The array to be sorted.
    """
    if array is None or len(array) <= 1:
        return  # No need to sort if the array is None, empty, or has one element.

    auxiliary_array = [0] * len(array)  # auxiliary array for merging
    merge_sort_rec(array, auxiliary_array, 0, len(array) - 1)


def merge_sort_rec(array, aux_array, start, end):
    """
    Recursive method that divides the array into halves, sorts them, and merges them.

    :param array: The array to be sorted.
    :param aux_array: Auxiliary array used for merging sorted halves.
    :param start: The starting index of the segment of the array to be sorted.
    :param end: The ending index of the segment of the array to be sorted.
    """
    if start < end:
        mid = (start + end) // 2
        merge_sort_rec(array, aux_array, start, mid)  # Sort the first half
        merge_sort_rec(array, aux_array, mid + 1, end)  # Sort the second half
        merge_both_parts(array, aux_array, start, mid + 1, end)  # Merge sorted halves


def merge_both_parts(array, aux_array, left, right, end):
    """
    Merges two sorted halves of the array.

    :param array: The original array containing all elements.
    :param aux_array: Auxiliary array used to help merge elements.
    :param left: The starting index of the first sorted half.
    :param right: The starting index of the second sorted half.
    :param end: The ending index of the second sorted half.
    """
    start = left
    mid = right - 1
    items_count = end - left + 1

    i = 0
    # Merge elements and store in aux_array
    while left <= mid and right <= end:
        if array[left] < array[right]:
            aux_array[i] = array[left]
            left += 1
        else:
            aux_array[i] = array[right]
            right += 1
        i += 1

    # Copy remaining elements from the first half
    while left <= mid:
        aux_array[i] = array[left]
        left += 1
        i += 1

    # Copy remaining elements from the second half
    while right <= end:
        aux_array[i] = array[right]
        right += 1
        i += 1

    # Copy back the merged elements to the original array
    for i in range(items_count):
        array[start + i] = aux_array[i]


def demo_merge_sort():
    """Demonstrates the usage of the merge sort function."""
    array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", array)

    merge_sort(array)

    print("Sorted array:", array)


if __name__ == "__main__":
    demo_merge_sort()
