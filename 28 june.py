# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

# Solution:
from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        row = 0
        col = cols - 1
        
        while row < rows and col >= 0:
            if grid[row][col] < 0:
                count += rows - row
                col -= 1
            else:
                row += 1
        
        return count



# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Solution:
from typing import List
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        for num, freq in counter.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        result = [item[1] for item in heap]
        result.reverse()
        
        return result

        

  
