# Given a string S. For each index i(1<=i<=N-1), erase it if s[i] is equal to s[i-1] in the string.

# Example 1:

# Input:
# S = aabb
# Output:  ab 
# Explanation: 'a' at 2nd position is appearing 2nd time consecutively.
# Similiar explanation for b at 4th position.


class Solution:
    def removeConsecutiveCharacter(self, S):
        # Initialize an empty string to store the result
        result = ""

        # Initialize a pointer to the first character
        i = 0
        n = len(S)

        while i < n:
            # Append the current character to the result
            result += S[i]

            # Find the next character that is different from the current one
            while i < n - 1 and S[i] == S[i + 1]:
                i += 1

            # Move to the next character
            i += 1

        return result

      
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # Create an empty stack to store opening brackets

        # Define a dictionary to map closing brackets to their corresponding opening brackets
        brackets_map = {')': '(', '}': '{', ']': '['}

        # Iterate through each character in the input string
        for char in s:
            # If it's an opening bracket, push it onto the stack
            if char in brackets_map.values():
                stack.append(char)
            # If it's a closing bracket
            elif char in brackets_map.keys():
                # Check if the stack is empty or if the top element of the stack matches the expected opening bracket
                if not stack or stack.pop() != brackets_map[char]:
                    return False

        # After iterating through the string, the stack should be empty if the string is valid
        return not stack
