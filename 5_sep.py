# Given a String S, reverse the string without reversing its individual words. Words are separated by dots.

# Example 1:

# Input:
# S = i.like.this.program.very.much
# Output: much.very.program.this.like.i
# Explanation: After reversing the whole
# string(not individual words), the input
# string becomes
# much.very.program.this.like.i

def reverseWords(s):
    words = s.split()
    
    reversed_words = words[::-1]
    
    reversed_string = ' '.join(reversed_words)
    
    return reversed_string
