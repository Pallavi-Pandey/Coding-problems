# You are given an array of characters letters that is sorted in non-decreasing order, and a character target. 
# There are at least two different characters in letters.
# Return the smallest character in letters that is lexicographically greater than target. 
# If such a character does not exist, return the first character in letters.

# Solution:
from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return letters[left % len(letters)]
