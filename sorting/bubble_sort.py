def bubble_sort(array):
    """Sorts an array using the Bubble Sort algorithm."""
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if array[j] > array[j + 1]:
                # Swap if they are in the wrong order
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        # If no two elements were swapped, the array is sorted
        if not swapped:
            break


def demo_bubble_sort():
    """Demonstrates the usage of the bubble sort function."""
    array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", array)

    bubble_sort(array)

    print("Sorted array:", array)


if __name__ == "__main__":
    demo_bubble_sort()
