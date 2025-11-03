"""
Problem: Remove Duplicates from Sorted List  
LeetCode #83  
Difficulty: Easy  
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/  

Problem Statement:  
Given the head of a sorted linked list, delete all duplicates such that  
each element appears only once. Return the linked list sorted as well.  

Examples:  
Input: head = [1,1,2]  
Output: [1,2]  

Input: head = [1,1,2,3,3]  
Output: [1,2,3]  

Approach (Single Pass):  
- Use a pointer `curr` starting at head.  
- Traverse the list:
  - While `curr.next` exists and `curr.val == curr.next.val`,  
    skip the duplicate by setting `curr.next = curr.next.next`.  
  - Move `curr` to the next unique node.  
- Return the modified head.  

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
        curr = head
        
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return head
