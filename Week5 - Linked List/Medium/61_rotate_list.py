"""
Problem: Rotate List  
LeetCode #61  
Difficulty: Medium  
Link: https://leetcode.com/problems/rotate-list/  

Problem Statement:  
Given the head of a linked list, rotate the list to the right by k places.  

Examples:  
Input: head = [1,2,3,4,5], k = 2  
Output: [4,5,1,2,3]  

Input: head = [0,1,2], k = 4  
Output: [2,0,1]  

Approach (Optimized):  
1. If list is empty or has one node → return head.  
2. Find the length of the list and the last node.  
3. Connect the last node to the head (make it circular).  
4. Compute `k = k % length` (rotating length times gives original list).  
5. Find the new tail: `(length - k - 1)`th node.  
6. The new head is the node after the new tail.  
7. Break the circle by setting new_tail.next = None.  

Time Complexity: O(n)  
Space Complexity: O(1)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # Step 1: Find length and last node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Make it circular
        tail.next = head

        # Step 3: Find new tail position
        k = k % length
        steps_to_new_tail = length - k - 1

        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None  # Break the circle

        return new_head
