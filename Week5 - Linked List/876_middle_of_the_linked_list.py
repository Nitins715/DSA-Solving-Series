"""
Problem: Middle of the Linked List  
LeetCode #876  
Difficulty: Easy  
Link: https://leetcode.com/problems/middle-of-the-linked-list/  

Problem Statement:  
Given the head of a singly linked list, return the middle node of the linked list.  
If there are two middle nodes, return the second middle node.  

Examples:  
Input: head = [1,2,3,4,5]  
Output: [3,4,5]  

Input: head = [1,2,3,4,5,6]  
Output: [4,5,6]  

Approach (Two Pointer — Fast and Slow):  
- Initialize two pointers: `slow` and `fast` starting at `head`.  
- Move `fast` by 2 steps and `slow` by 1 step each iteration.  
- When `fast` reaches the end, `slow` will be at the middle node.  
- Return `slow` as the head of the second half (middle node).  

Time Complexity: O(n)  
Space Complexity: O(1)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head):
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
