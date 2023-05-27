# Question 2      
# 1486. XOR Operation in an Array
# https://leetcode.com/problems/xor-operation-in-an-array/

# You are given an integer n and an integer start.
# Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.
# Return the bitwise XOR of all elements of nums.
# Example 1:

# Input: n = 5, start = 0
# Output: 8
# Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
# Where "^" corresponds to bitwise XOR operator.

#Solution
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        for i in range(n):
            res ^= start + 2 * i
        return res

      
# Question 2      
# Making File Names Unique
# https://leetcode.com/problems/making-file-names-unique/

# Given an array of strings names of size n. You will create n folders in your file system such that, at the ith minute, you will create a folder with the name names[i].
# Since two files cannot have the same name, if you enter a folder name that was previously used, the system will have a suffix addition to its name in the form of (k), 
# where, k is the smallest positive integer such that the obtained name remains unique.
# Return an array of strings of length n where ans[i] is the actual name the system will assign to the ith folder when you create it.  

#Solution
from collections import defaultdict as maps
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        d = maps(int); n = len(names)
        for i in range(n):
            if (d[names[i]]):
                val = names[i] + "(" + str(d[names[i]]) + ")"
                while val in d:
                    d[names[i]] += 1;
                    val = names[i] + "(" + str(d[names[i]]) + ")"
                d[val] += 1; names[i] = val;
            else:
                d[names[i]] += 1;
        return names
