# 1496. Path Crossing
# https://leetcode.com/problems/path-crossing/

# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. 
# You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.
# Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

# solution
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        seen = {(0, 0)}
        a, b = 0, 0
        directions = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}

        for char in path:
            a, b = a + directions[char][0], b + directions[char][1]

            if (a, b) in seen:
                return True

            seen.add((a, b))

        return False
      
# 1497. Check If Array Pairs Are Divisible by k
# https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/
  
# Given an array of integers arr of even length n and an integer k.
# We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.
# Return true If you can find a way to do that or false otherwise.

# solution
from collections import defaultdict

class Solution:
    def canArrange(self, arr, k):
        remainder_counts = defaultdict(int)

        for num in arr:
            remainder = num % k
            remainder_counts[remainder] += 1

        if remainder_counts[0] % 2 != 0:
            # If the count of elements with remainder 0 is odd, pairs cannot be formed.
            return False

        for remainder in range(1, k // 2 + 1):
            # We are checking if there are equal counts of elements with remainders remainder and k - remainder
            if remainder_counts[remainder] != remainder_counts[k - remainder]:
                return False

        if k % 2 == 0 and remainder_counts[k // 2] % 2 != 0:
            # If k is even, the count of elements with remainder k/2 should be even
            return False

        return True
