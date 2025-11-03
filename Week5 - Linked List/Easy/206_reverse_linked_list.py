"""
Problem: Reverse Linked List  
LeetCode #206  
Difficulty: Easy  
Link: https://leetcode.com/problems/reverse-linked-list/  

Problem Statement:  
Given the head of a singly linked list, reverse the list,  
and return the reversed list.

Examples:  
Input: head = [1,2,3,4,5]  
Output: [5,4,3,2,1]  

Input: head = [1,2]  
Output: [2,1]  

Input: head = []  
Output: []  

Approach (Iterative):  
- Initialize three pointers: `prev = None`, `curr = head`, `next = None`.  
- Traverse the list:
  - Store the next node (`next = curr.next`).  
  - Reverse the link (`curr.next = prev`).  
  - Move `prev` and `curr` one step forward.  
- When the loop ends, `prev` will be the new head of the reversed list.  
- Return `prev`.

Time Complexity: O(n)  
Space Complexity: O(1)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev
