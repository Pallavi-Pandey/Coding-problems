# 1502. Can Make Arithmetic Progression From Sequence
# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
  
# A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.
# Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.
# Example 1:

# Input: arr = [3,5,1]
# Output: true
# Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.

# solution
from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)
        if n <= 2:
            return True
        arr.sort()
        diff = arr[1] - arr[0]  # Calculate the common difference
        for i in range(2, n):
            if arr[i] - arr[i-1] != diff:
                return False

        return True
