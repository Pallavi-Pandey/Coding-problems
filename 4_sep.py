# https://practice.geeksforgeeks.org/problems/max-min/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab

# Given an array A of size N of integers. 
# Your task is to find the sum of minimum and maximum element in the array.

# Example 1:

# Input:
# N = 5
# A[] = {-2, 1, -4, 5, 3}
# Output: 1
# Explanation: min = -4, max =  5. Sum = -4 + 5 = 1

# Sorting Algorithm
def maxMin(N, arr):
    # Step 2: Sort the array
    arr.sort()

    # Step 3: Calculate the minimum and maximum values
    minimum = arr[0]
    maximum = arr[N - 1]

    # Step 4: Calculate the result
    result = maximum - minimum

    return result

# Example usage
N = 5
arr = [1, 3, 5, 7, 9]
result = maxMin(N, arr)
print("Maximum difference:", result)


# Linear Algorithm
def maxMin(N, arr):
    if N == 0:
        return None  # Handle the case of an empty array

    # Step 1: Initialize minimum and maximum
    minimum = maximum = arr[0]

    # Step 2: Iterate through the array
    for i in range(1, N):
        # Step 3: Update minimum and maximum
        if arr[i] < minimum:
            minimum = arr[i]
        elif arr[i] > maximum:
            maximum = arr[i]

    # Step 4: Return the minimum and maximum values
    return maximum - minimum

