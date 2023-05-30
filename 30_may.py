#1504. Count Submatrices With All Ones
#https://leetcode.com/problems/count-submatrices-with-all-ones/

#Given an m x n binary matrix mat, return the number of submatrices that have all ones.

#Solution
from typing import List

class Solution:
    def countSubmatrices(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        count = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    for k in range(i, -1, -1):
                        width = cols
                        for l in range(j, -1, -1):
                            if matrix[k][l] == 1:
                                count += 1
                                width = min(width, j - l + 1)
                            else:
                                break
                            count += width
        return count
