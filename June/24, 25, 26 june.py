# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. 
# Then return the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
# The remaining elements of nums are not important as well as the size of nums.
# Return k.

# Solution :
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pos = 0
        for num in nums:
            if num != val:
                nums[pos] = num
                pos += 1
        
        return pos


# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Solution:
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]



# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

# Solution:
class Solution:
    def getMinimumDifference(self, root):
        self.prev = None 
        self.min_diff = float('inf')  
        def inorder(node):
            if node is None:
                return
            
            # Traverse the left subtree
            inorder(node.left)
            
            # Calculating the absolute difference between the current node and the previous node
            if self.prev is not None:
                self.min_diff = min(self.min_diff, abs(node.val - self.prev))
            self.prev = node.val
            inorder(node.right)
        inorder(root)
        
        return self.min_diff


# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Solution:
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        count = 0
        for num in nums:
            if num == candidate:
                count += 1
        
        return candidate if count > len(nums) // 2 else -1
