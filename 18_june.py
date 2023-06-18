# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range 
# [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Solution:
class Solution:
    def reverse(self, x: int) -> int:
        # Check if the given number is negative
        is_negative = True if x < 0 else False
        
        # Convert the number to a positive value for reversal
        x = abs(x)
        
        # Initialize the reversed number
        reversed_num = 0
        
        while x > 0:
            # Extract the last digit of the number
            digit = x % 10
            
            # Append the digit to the reversed number
            reversed_num = reversed_num * 10 + digit
            
            # Remove the last digit from the number
            x //= 10
        
        # Apply the sign to the reversed number
        reversed_num = -reversed_num if is_negative else reversed_num
        
        # Check for integer overflow
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        
        return reversed_num
