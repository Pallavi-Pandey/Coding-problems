# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false


from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        unique_elements = set()
        
        for num in nums: 
            if num in unique_elements:
                return True
            unique_elements.add(num)
        
        return False
