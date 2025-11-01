"""
Problem: Merge Two Sorted Lists  
LeetCode #21  
Difficulty: Easy  
Link: https://leetcode.com/problems/merge-two-sorted-lists/  

Problem Statement:  
You are given the heads of two sorted linked lists, list1 and list2.  
Merge the two lists into one sorted linked list and return its head.  

Examples:  
Input: list1 = [1,2,4], list2 = [1,3,4]  
Output: [1,1,2,3,4,4]  

Input: list1 = [], list2 = []  
Output: []  

Input: list1 = [], list2 = [0]  
Output: [0]  

Approach (Iterative with Dummy Node):  
- Create a dummy node to simplify list merging.  
- Use a pointer `tail` to track the end of the merged list.  
- Compare the current nodes of both lists:
  - Append the smaller node to `tail.next`.  
  - Move that list’s pointer forward.  
- When one list is exhausted, attach the remaining nodes of the other list.  
- Return `dummy.next` as the merged list’s head.  

Time Complexity: O(n + m)  
Space Complexity: O(1)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        tail.next = list1 if list1 else list2
        
        return dummy.next
