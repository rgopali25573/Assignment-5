import random
import time


def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot_index = random.randint(0, len(arr) - 1)
        pivot = arr[pivot_index]
        smaller = [x for x in arr if x < pivot]
        greater = [x for x in arr if x > pivot]
        pivots = [x for x in arr if x == pivot]  # to handle duplicates
        return randomized_quicksort(smaller) + pivots + randomized_quicksort(greater)

def quicksort(arr):#deterministic_quicksort
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]  # choosing the last element as the pivot
        smaller = [x for x in arr[:-1] if x <= pivot]
        greater = [x for x in arr[:-1] if x > pivot]
        return quicksort(smaller) + [pivot] + quicksort(greater)

def measure_time(sort_func, arr):
    start = time.time()
    sort_func(arr)
    return time.time() - start

# Generate input arrays
sizes = [1000, 5000, 10000, 20000]
distributions = {
    "random": lambda n: [random.randint(0, n) for _ in range(n)],
    "sorted": lambda n: list(range(n)),
    "reverse_sorted": lambda n: list(range(n, 0, -1))
}

# Test both versions of Quicksort
for size in sizes:
    for dist_name, dist_func in distributions.items():
        arr = dist_func(size)
        dt_time = measure_time(quicksort, arr.copy())
        rand_time = measure_time(randomized_quicksort, arr.copy())
        print(f"Size: {size}, Distribution: {dist_name}, "
              f"Deterministic: {dt_time:.5f}s, Randomized: {rand_time:.5f}s")