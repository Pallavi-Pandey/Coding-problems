# Given an array A[ ] of positive integers of size N, where each value represents the number of chocolates in a packet. 
# Each packet can have a variable number of chocolates. 
# There are M students, the task is to distribute chocolate packets among M students such that :
# 1. Each student gets exactly one packet.
# 2. The difference between maximum number of chocolates given to a student and minimum number of chocolates given to a student is minimum.

# Example 1:

# Input:
# N = 8, M = 5
# A = {3, 4, 1, 9, 56, 7, 9, 12}
# Output: 6
# Explanation: The minimum difference between maximum chocolates and minimum chocolates is 9 - 3 = 6 by choosing following M packets 
# :{3, 4, 9, 7, 9}.


class Solution:
    def findMinDiff(self, A, N, M):
        # Sorting of the array in ascending order
        A.sort()
        
        # Initializing min_diff with a large value
        min_diff = float('inf')
        
        for i in range(N - M + 1):
            current_diff = A[i + M - 1] - A[i]
            min_diff = min(min_diff, current_diff)
        
        return min_diff

# Driver code
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())
        solObj = Solution()
        print(solObj.findMinDiff(A, N, M))
