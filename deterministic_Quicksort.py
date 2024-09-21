def quicksort(arr):
    # Define the Quicksort function, taking 'arr' (the array to be sorted) as input.

    if len(arr) <= 1:
        # Base case: if the array has 1 or 0 elements, it is already sorted, so return it as is.
        return arr

    else:
        pivot = arr[-1]
        # Choose the last element of the array as the pivot.

        smaller = [x for x in arr[:-1] if x <= pivot]
        # Create a list of elements smaller than or equal to the pivot (ignoring the pivot itself).

        greater = [x for x in arr[:-1] if x > pivot]
        # Create a list of elements greater than the pivot.

        return quicksort(smaller) + [pivot] + quicksort(greater)
        # Recursively apply Quicksort to the 'smaller' and 'greater' subarrays,
        # and combine the sorted 'smaller' array, the pivot, and the sorted 'greater' array.
