# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Solution:
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set = set(nums)  
        longest_seq = 0
        
        for num in num_set:
            # Check if num - 1 exists in the set
            if num - 1 not in num_set:
                current_num = num
                current_seq = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_seq += 1
                
                longest_seq = max(longest_seq, current_seq)
        
        return longest_seq

      
# You are given a sorted unique integer array nums.
# A range [a,b] is the set of all integers from a to b (inclusive).
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
# Each range [a,b] in the list should be output as:
# "a->b" if a != b
# "a" if a == b

# Solution:
from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        result = []
        start = nums[0]  # Initialize the start of the current range
        
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 1:
                result.append(self.formatRange(start, nums[i-1]))
                start = nums[i]
        result.append(self.formatRange(start, nums[-1]))       
        return result
    
    def formatRange(self, start: int, end: int) -> str:
        if start == end:
            return str(start)
        else:
            return str(start) + "->" + str(end)
  
