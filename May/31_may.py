# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# solution

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_indices:
                return [num_indices[complement], i]
            num_indices[num] = i

        return []  

# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Solution

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        char_set = set()
        left = 0
        right = 0
        max_length = 0

        while right < n:
            if s[right] not in char_set:
                char_set.add(s[right])
                max_length = max(max_length, right - left + 1)
                right += 1
            else:
                char_set.remove(s[left])
                left += 1

        return max_length
