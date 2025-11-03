"""
Problem: Swap Nodes in Pairs  
LeetCode #24  
Difficulty: Medium  
Link: https://leetcode.com/problems/swap-nodes-in-pairs/  

Problem Statement:  
Given a linked list, swap every two adjacent nodes and return its head.  
You must solve the problem without modifying the values in the list's nodes  
(i.e., only nodes themselves may be changed).  

Examples:  
Input: head = [1,2,3,4]  
Output: [2,1,4,3]  

Input: head = []  
Output: []  

Input: head = [1]  
Output: [1]  

Approach (Iterative - Dummy Node):  
1. Create a dummy node pointing to head for easier edge handling.  
2. Use `prev` pointer to track node before the pair to be swapped.  
3. For each pair (first, second):  
   - Adjust pointers to swap them:  
     `prev.next = second`, `first.next = second.next`, `second.next = first`.  
   - Move `prev` forward by two nodes.  
4. Continue until no more pairs left.  

Time Complexity: O(n)  
Space Complexity: O(1)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head and head.next:
            first = head
            second = head.next

            # Swap
            prev.next = second
            first.next = second.next
            second.next = first

            # Move pointers forward
            prev = first
            head = first.next

        return dummy.next
