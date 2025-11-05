"""
Problem: Add Two Numbers  
LeetCode #2  
Difficulty: Medium  
Link: https://leetcode.com/problems/add-two-numbers/  

Problem Statement:  
You are given two non-empty linked lists representing two non-negative integers.  
The digits are stored in reverse order, and each node contains a single digit.  
Add the two numbers and return the sum as a linked list.  

You may assume the two numbers do not contain any leading zero, except the number 0 itself.  

Examples:  
Input: l1 = [2,4,3], l2 = [5,6,4]  
Output: [7,0,8]  
Explanation: 342 + 465 = 807  

Approach (Optimized Iterative with Carry):  
- Use a dummy head to simplify list operations.  
- Traverse both lists while any of them or carry exists.  
- At each step:
  - sum = l1.val (if available) + l2.val (if available) + carry  
  - carry = sum // 10  
  - new node value = sum % 10  
- Move pointers ahead.  
- Return dummy.next as the result.  

Time Complexity: O(max(m, n))  
Space Complexity: O(1) — excluding the output list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)

            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
