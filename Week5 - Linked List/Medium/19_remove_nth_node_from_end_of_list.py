"""
Problem: Remove Nth Node From End of List  
LeetCode #19  
Difficulty: Medium  
Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/  

Problem Statement:  
Given the head of a linked list, remove the n-th node from the end of the list and return its head.  

Examples:  
Input: head = [1,2,3,4,5], n = 2  
Output: [1,2,3,5]  

Input: head = [1], n = 1  
Output: []  

Input: head = [1,2], n = 1  
Output: [1]  

Approach (Two-Pointer Technique):  
1. Create a dummy node pointing to `head` (helps handle edge cases).  
2. Initialize two pointers: `first` and `second` at dummy.  
3. Move `first` ahead by `n + 1` steps.  
4. Move both pointers one step at a time until `first` reaches the end.  
5. Now, `second` points to the node before the one to delete.  
6. Update `second.next = second.next.next` to remove the node.  
7. Return `dummy.next` as the new head.  

Time Complexity: O(n)  
Space Complexity: O(1)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        first = second = dummy

        # Step 1: Move first n+1 steps ahead
        for _ in range(n + 1):
            first = first.next

        # Step 2: Move both until first reaches end
        while first:
            first = first.next
            second = second.next

        # Step 3: Remove nth node
        second.next = second.next.next

        return dummy.next
