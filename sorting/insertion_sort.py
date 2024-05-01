def insertion_sort(array):
    """Sorts the provided array using the Insertion Sort algorithm."""
    for i in range(1, len(array)):
        temp = array[i]

        # Move elements of array[0..i-1] that are greater than the temp
        # to one position ahead of their current position
        j = i
        while j > 0 and array[j - 1] > temp:
            array[j] = array[j - 1]
            j -= 1
        array[j] = temp


def demo_insertion_sort():
    """Demonstrates the usage of the Insertion Sort function."""
    array = [64, 25, 12, 22, 11, 90, 18]
    print("Original array:", array)

    insertion_sort(array)

    print("Sorted array:", array)


# Example usage
if __name__ == "__main__":
    demo_insertion_sort()
