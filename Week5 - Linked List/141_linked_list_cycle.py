"""
Problem: Linked List Cycle  
LeetCode #141  
Difficulty: Easy  
Link: https://leetcode.com/problems/linked-list-cycle/  

Problem Statement:  
Given the head of a linked list, determine if the linked list has a cycle in it.  

There is a cycle in a linked list if there is some node in the list  
that can be reached again by continuously following the `next` pointer.  
Return true if there is a cycle in the linked list. Otherwise, return false.  

Examples:  
Input: head = [3,2,0,-4], pos = 1  
Output: true  
Explanation: The tail connects to the second node.  

Input: head = [1,2], pos = 0  
Output: true  

Input: head = [1], pos = -1  
Output: false  

Approach (Floyd’s Cycle Detection Algorithm — Tortoise and Hare):  
- Use two pointers: `slow` and `fast`.  
- Move `slow` by one step and `fast` by two steps in each iteration.  
- If at any point `slow == fast`, a cycle exists.  
- If `fast` or `fast.next` becomes `None`, there is no cycle.  

Time Complexity: O(n)  
Space Complexity: O(1)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head):
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False
