# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, 
# and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Solution:
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()  # Dummy node to hold the result
        curr = dummy  # Current node for constructing the result
        carry = 0  # Carry value for addition
        
        while l1 or l2 or carry:
            # Calculate the sum of current digits and carry value
            sum_val = carry
            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next
            
            carry = sum_val // 10  # Determine the carry value
            digit = sum_val % 10  # Determine the current digit
            
            curr.next = ListNode(digit)  # Create a new node for the current digit
            curr = curr.next
        
        return dummy.next  # Return the result linked list starting from the next node of the dummy
