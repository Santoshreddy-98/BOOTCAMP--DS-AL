def merge_sort(arr):
    """
    Sorts an array using the Merge Sort algorithm.

    Parameters:
    - arr (list): List of elements to be sorted.

    Returns:
    - list: Sorted list.
    """
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle of the array
        left_half = arr[:mid]  # Divide the array into two halves
        right_half = arr[mid:]

        # Recursively sort the two halves
        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0

        # Merge the sorted halves back into the original array
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check for any remaining elements in the left and right halves
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Example usage:
unsorted_list = [64, 34, 25, 12, 22, 11, 90]

# Sort the list using Merge Sort
sorted_list = merge_sort(unsorted_list)

# Display the result
print("Sorted array:", sorted_list)
