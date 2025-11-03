"""
Problem: Reorder List  
LeetCode #143  
Difficulty: Medium  
Link: https://leetcode.com/problems/reorder-list/  

Problem Statement:  
You are given the head of a singly linked list.  
Reorder the list to follow this specific pattern:  
L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …  

You must do this in-place without modifying the nodes' values.

Examples:  
Input: head = [1,2,3,4]  
Output: [1,4,2,3]  

Input: head = [1,2,3,4,5]  
Output: [1,5,2,4,3]  

Approach (3-Step Optimal Solution):  
1. **Find Middle:** Use slow & fast pointers to find the middle of the list.  
2. **Reverse Second Half:** Reverse the second half of the list in place.  
3. **Merge Two Halves:** Alternate nodes from the first and second halves.  

This ensures in-place modification with O(1) extra space.  

Time Complexity: O(n)  
Space Complexity: O(1)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return

        # Step 1: Find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        prev, curr = None, slow.next
        slow.next = None  # Split list
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Step 3: Merge two halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
