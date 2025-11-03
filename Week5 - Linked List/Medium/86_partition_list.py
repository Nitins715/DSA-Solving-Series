"""
Problem: Partition List  
LeetCode #86  
Difficulty: Medium  
Link: https://leetcode.com/problems/partition-list/  

Problem Statement:  
Given the head of a linked list and a value x,  
partition it such that all nodes less than x come before nodes greater than or equal to x.  

You should preserve the original relative order of the nodes in each partition.  

Examples:  
Input: head = [1,4,3,2,5,2], x = 3  
Output: [1,2,2,4,3,5]  

Input: head = [2,1], x = 2  
Output: [1,2]  

Approach (Two Dummy Lists):  
1. Create two dummy lists:  
   - `before` list for nodes < x  
   - `after` list for nodes >= x  
2. Traverse through the list:  
   - Append each node to the correct list.  
3. Connect the `before` list to the `after` list.  
4. Ensure the end of `after` list points to `None`.  

This maintains stability (original order) and uses O(1) extra space.  

Time Complexity: O(n)  
Space Complexity: O(1)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head, x):
        before_head = ListNode(0)
        after_head = ListNode(0)
        before = before_head
        after = after_head

        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next

        after.next = None  # Important: prevent cycle
        before.next = after_head.next

        return before_head.next
