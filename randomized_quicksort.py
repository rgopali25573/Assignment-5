import random


def randomized_quicksort(arr):
    # Define the Randomized Quicksort function, taking 'arr' (the array to be sorted) as input.

    if len(arr) <= 1:
        # Base case: if the array has 1 or 0 elements, it's already sorted, so return it as is.
        return arr

    else:
        # Recursive case: if the array has more than 1 element, proceed with sorting.

        pivot_index = random.randint(0, len(arr) - 1)
        # Randomly select a pivot index between 0 and the last index of the array.

        pivot = arr[pivot_index]
        # Set the pivot element using the randomly chosen pivot index.

        smaller = [x for x in arr if x < pivot]
        # Create a list of elements that are smaller than the pivot.

        greater = [x for x in arr if x > pivot]
        # Create a list of elements that are greater than the pivot.

        pivots = [x for x in arr if x == pivot]
        # Handle duplicates: create a list of elements that are equal to the pivot.

        return randomized_quicksort(smaller) + pivots + randomized_quicksort(greater)
        # Recursively sort the 'smaller' and 'greater' subarrays,
        # then concatenate the sorted 'smaller' array, the pivot list, and the sorted 'greater' array.
