# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Your Solution class
class Solution:
    def maxSubArray(self, nums):
        max_sum = float('-inf')  # Initialize max_sum to negative infinity
        current_sum = 0

        for num in nums:
            current_sum += num
            max_sum = max(max_sum, current_sum)

            if current_sum < 0:
                current_sum = 0

        return max_sum

# Driver code
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        nums = list(map(int, input().split()))
        obj = Solution()
        print(obj.maxSubArray(nums))
