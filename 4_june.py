# 9. Palindrome Number
# Given an integer x, return true if x is a palindrome, and false otherwise.

# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Solution
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        reverse = 0
        temp = x
        
        while temp > 0:
            reverse = (reverse * 10) + (temp % 10)
            temp //= 10
        
        return reverse == x

# 13. Roman to Integer
# Given a roman numeral, convert it to an integer.
# Solution
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

        total = 0
        prev_value = 0

        for char in s[::-1]:
            curr_value = roman_map[char]

            if curr_value < prev_value:
                total -= curr_value
            else:
                total += curr_value

            prev_value = curr_value

        return total
