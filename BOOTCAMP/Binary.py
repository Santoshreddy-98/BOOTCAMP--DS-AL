def binary_search(arr, target):
    """
    Perform binary search on a sorted array.

    Parameters:
    - arr (list): Sorted list of elements.
    - target: Element to search for.

    Returns:
    - int: Index of the target element if found, -1 otherwise.
    """
    low, high = 0, len(arr) - 1  # Set initial search range

    while low <= high:
        mid = (low + high) // 2  # Calculate mid-point

        if arr[mid] == target:
            return mid  # Target found, return its index
        elif arr[mid] < target:
            low = mid + 1  # Adjust the search range to the right half
        else:
            high = mid - 1  # Adjust the search range to the left half

    return -1  # Target not found

# Example usage:
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_element = 3

# Perform binary search
result = binary_search(sorted_list, target_element)

# Display the result
if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the list.")
