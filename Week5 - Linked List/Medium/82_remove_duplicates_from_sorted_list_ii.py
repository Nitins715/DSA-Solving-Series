"""
Problem: Remove Duplicates from Sorted List II  
LeetCode #82  
Difficulty: Medium  
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/  

Problem Statement:  
Given the head of a sorted linked list, delete all nodes that have duplicate numbers,  
leaving only distinct numbers from the original list.  
Return the linked list sorted as well.  

Examples:  
Input: head = [1,2,3,3,4,4,5]  
Output: [1,2,5]  

Input: head = [1,1,1,2,3]  
Output: [2,3]  

Approach (Dummy Node + Pointer Traversal):  
1. Use a dummy node before the head to handle edge cases easily.  
2. Use two pointers: `prev` (points to the last non-duplicate node) and `current`.  
3. If duplicates are found (current.val == current.next.val),  
   skip all nodes with that value.  
4. Otherwise, move `prev` forward normally.  
5. Continue until end of list.  

Time Complexity: O(n)  
Space Complexity: O(1)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(0, head)
        prev = dummy

        while head:
            # Check for duplicates
            if head.next and head.val == head.next.val:
                duplicate_val = head.val
                # Skip all nodes with this value
                while head and head.val == duplicate_val:
                    head = head.next
                prev.next = head
            else:
                prev = prev.next
                head = head.next

        return dummy.next
