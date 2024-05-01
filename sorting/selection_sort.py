def selection_sort(array):
    """Sorts the provided array using the Selection Sort algorithm."""
    n = len(array)
    # Move through the unsorted part of the array
    for i in range(n - 1):
        # Assume the first element is the minimum
        min_index = i
        # Check the rest of the array to find the true minimum
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j  # Found a new minimum, remember its index

        # Swap the minimum element with the first element of the unsorted section
        array[min_index], array[i] = array[i], array[min_index]


def demo_selection_sort():
    """Demonstrates the usage of the Selection Sort function."""
    array = [64, 25, 12, 22, 11, 90, 18]
    print("Original array:", array)

    selection_sort(array)

    print("Sorted array:", array)


# Example usage
if __name__ == "__main__":
    demo_selection_sort()
