"""
Problem: Odd Even Linked List  
LeetCode #328  
Difficulty: Medium  
Link: https://leetcode.com/problems/odd-even-linked-list/  

Problem Statement:  
Given the head of a singly linked list, group all the nodes with odd indices together  
followed by the nodes with even indices, and return the reordered list.  

The first node is considered odd, the second even, and so on.  
You must do this in-place and maintain the relative order within both groups.

Examples:  
Input: head = [1,2,3,4,5]  
Output: [1,3,5,2,4]  

Input: head = [2,1,3,5,6,4,7]  
Output: [2,3,6,7,1,5,4]  

Approach (Two-Pointer Technique):  
- Maintain two pointers: `odd` (for odd indices) and `even` (for even indices).  
- Also, keep a reference to `even_head` to reconnect later.  
- Traverse through the list, re-linking nodes alternatively.  
- At the end, link the last odd node to `even_head`.  

Time Complexity: O(n)  
Space Complexity: O(1)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even  # To reconnect later

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head
