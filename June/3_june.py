# 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Solution
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in parentheses_map.values():
                stack.append(char)
            elif char in parentheses_map.keys():
                if not stack or stack.pop() != parentheses_map[char]:
                    return False
            else:
                return False

        return len(stack) == 0

# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Solution

from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        min_length = min(len(s) for s in strs)
        prefix = ""

        for i in range(min_length):
            char = strs[0][i]
            if all(s[i] == char for s in strs):
                prefix += char
            else:
                break

        return prefix
