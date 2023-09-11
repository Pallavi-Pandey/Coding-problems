#1480. Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).Return the running sum of nums.
#Example 1:
#Input: nums = [1,2,3,4]
#Output: [1,3,6,10]
#Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

##solution
from ast import List
from collections import Counter


class Solution:
    def runningSum(self, nums):
        output = [0] * len(nums)
        output[0] = nums[0]
        for i in range(1, len(nums)):
            output[i] = output[i - 1] + nums[i]
        return output


#1481. Least Number of Unique Integers after K Removals 
# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/
#Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.
#Example 1:

# Input: arr = [5,5,4], k = 1
# Output: 1
# Explanation: Remove the single 4, only 5 is left.

##solution
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        cnt, remaining = Counter(c.values()), len(c)
        for key in sorted(cnt): 
            if k >= key * cnt[key]:
                k -= key * cnt[key]
                remaining -= cnt.pop(key)
            else:
                return remaining - k // key
        return remaining
