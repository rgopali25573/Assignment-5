# Quicksort Implementation and Analysis

This project implements and compares two versions of the Quicksort algorithm: a deterministic version and a randomized version. It also includes a script to measure and compare the running times of both implementations.

## Files

1. `deterministic_quicksort.py`: Contains the implementation of the deterministic Quicksort algorithm.
2. `randomized_quicksort.py`: Contains the implementation of the randomized Quicksort algorithm.
3. `runningtime_quicksort_versions.py`: Script to measure and compare the running times of both Quicksort implementations.

## How to Run the Code

1. Ensure you have Python installed on your system.
2. Download all three Python files into the same directory.
3. Open a terminal or command prompt and navigate to the directory containing the files.
4. Run the performance comparison script using the following command:

   ```
   python runningtime_quicksort_versions.py
   ```

5. The script will output the running times for both Quicksort versions with different input sizes and distributions.

## Summary of Findings

The performance analysis of the deterministic and randomized Quicksort implementations revealed the following key points:

1. **Average Case Performance**: Both versions of Quicksort demonstrated an average-case time complexity of O(n log n), which is optimal for comparison-based sorting algorithms.

2. **Impact of Randomization**: The randomized version of Quicksort showed more consistent performance across different input distributions. This is because it reduces the likelihood of encountering worst-case scenarios.

3. **Best Case Scenario**: In the best case, both versions achieve O(n log n) time complexity. This occurs when the pivot consistently divides the array into two nearly equal subarrays.

4. **Worst Case Scenario**: The deterministic version can degrade to O(n^2) in worst-case scenarios, particularly with already sorted or reverse-sorted arrays. The randomized version mitigates this risk.

5. **Performance on Different Distributions**:
   - Random Distribution: Both versions performed similarly.
   - Sorted and Reverse-Sorted Arrays: The randomized version showed more consistent performance, while the deterministic version was more susceptible to worst-case behavior.

6. **Scalability**: Both algorithms showed good scalability with increasing input sizes, maintaining their expected time complexities.

7. **Practical Implications**: For most general-purpose sorting tasks, the randomized version is preferred due to its more consistent performance across various input distributions.

8. **Trade-offs**: The randomized version introduces a small overhead due to the random number generation, but this is generally outweighed by the benefits of avoiding worst-case scenarios.

In conclusion, while both implementations are effective, the randomized Quicksort offers more robust performance across different input types and sizes, making it a safer choice for general-purpose sorting tasks.
