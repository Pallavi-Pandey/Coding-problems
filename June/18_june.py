# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range 
# [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Solution:
class Solution:
    def reverse(self, x: int) -> int:
        is_negative = True if x < 0 else False
        x = abs(x
        reversed_num = 0
        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
        reversed_num = -reversed_num if is_negative else reversed_num
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        
        return reversed_num
