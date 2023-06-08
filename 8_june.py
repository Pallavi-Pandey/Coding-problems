# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# solution
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter_s = Counter(s)
        counter_t = Counter(t)

        return counter_s == counter_t

# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. 
# Check if these points make a straight line in the XY plane.
# Solution
from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if (x1 - x0) * (y - y0) != (x - x0) * (y1 - y0):
                return False

        return True
