"""
Problem: Add Two Numbers II  
LeetCode #445  
Difficulty: Medium  
Link: https://leetcode.com/problems/add-two-numbers-ii/  

Problem Statement:  
You are given two non-empty linked lists representing two non-negative integers.  
The most significant digit comes first, and each node contains a single digit.  
Add the two numbers and return the sum as a linked list.  

You may assume the two numbers do not contain any leading zero, except the number 0 itself.  

Examples:  
Input: l1 = [7,2,4,3], l2 = [5,6,4]  
Output: [7,8,0,7]  
Explanation: 7243 + 564 = 7807  

Approach (Using Stacks):  
- Since the digits are in forward order, we can’t simply traverse from tail to head.  
- Use two stacks to reverse the order of both lists.  
- Pop elements from both stacks, add them with carry.  
- Create new nodes for each digit and prepend them to the result list.  

Steps:  
1. Push all digits of l1 and l2 into two stacks.  
2. Initialize carry = 0.  
3. While either stack or carry exists:
   - Pop values if available.
   - Compute sum = v1 + v2 + carry.
   - carry = sum // 10.
   - Create new node with sum % 10 and insert it at the front of the result list.
4. Return head of the resulting linked list.  

Time Complexity: O(m + n)  
Space Complexity: O(m + n)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        stack1, stack2 = [], []

        # Push all values to stacks
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        head = None

        # Process both stacks
        while stack1 or stack2 or carry:
            v1 = stack1.pop() if stack1 else 0
            v2 = stack2.pop() if stack2 else 0

            total = v1 + v2 + carry
            carry = total // 10

            # Create new node and add it at front
            node = ListNode(total % 10)
            node.next = head
            head = node

        return head
