# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]],
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Solution
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  
        triplets = []
        for i in range(len(nums) - 2):
            # Skipping duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]  # Setting the target to find with two pointers
            left = i + 1
            right = len(nums) - 1

            while left < right:
                # Calculating the sum of the current triplet
                current_sum = nums[left] + nums[right]

                if current_sum < target:
                    left += 1  # Incrementing left pointer if sum is too small
                elif current_sum > target:
                    right -= 1  # Decrementing right pointer if sum is too large
                else:
                    # Find a triplet that sums up to zero
                    triplets.append([nums[i], nums[left], nums[right]])

                    # Skipping duplicates for the second and third elements
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1  # Moveing the left pointer to the next distinct element
                    right -= 1  # Moveing the right pointer to the next distinct element

        return triplets
