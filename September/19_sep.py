# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

# For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.

# The replacement must be in place and use only constant extra memory.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [1,3,2]

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # Step 1: Find the first element from the right that is smaller than the next element.
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # Step 2: If such an element is found, find the smallest element to the right of i that is greater than nums[i].
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Swap nums[i] and nums[j].
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: Reverse the subarray to the right of i.
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


# Given two arrays of equal size N and an integer K. The task is to check if after permuting both arrays, 
# we get sum of their corresponding element greater than or equal to k i.e Ai + Bi >= K for all i (from 0 to N-1). Return true if possible, else false.
 
# Example 1:

# Input : 
# a[] = {2, 1, 3}, 
# b[] = { 7, 8, 9 }, 
# k = 10. 
# Output : 
# True
# Explanation:
# Permutation  a[] = { 1, 2, 3 } 
# and b[] = { 9, 8, 7 } 
# satisfied the condition a[i] + b[i] >= K.

class Solution:
    def isPossible(self, a, b, n, k):
        # Create a sorted copy of array 'a'
        sorted_a = sorted(a)
        
        # Initialize a variable to keep track of the number of elements that satisfy the condition
        count = 0
        
        # Iterate through the arrays 'a' and 'sorted_a'
        for i in range(n):
            # If the absolute difference between the current element and its index is at most 'k',
            # increment the count and remove the element from 'sorted_a'
            if abs(a[i] - i) <= k and sorted_a:
                sorted_a.pop(0)
                count += 1
        
        # If the count is equal to 'n', it means all elements satisfy the condition
        return count == n
