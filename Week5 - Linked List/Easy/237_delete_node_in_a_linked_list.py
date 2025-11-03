"""
Problem: Delete Node in a Linked List  
LeetCode #237  
Difficulty: Easy  
Link: https://leetcode.com/problems/delete-node-in-a-linked-list/  

Problem Statement:  
There is a singly linked list, and you are given the node to be deleted (not the tail node).  
Delete the given node from the linked list directly without access to the head.  

Examples:  
Input: head = [4,5,1,9], node = 5  
Output: [4,1,9]  

Input: head = [4,5,1,9], node = 1  
Output: [4,5,9]  

Approach:  
Since we cannot access the previous node, we can copy the next node’s data  
into the current node and then delete the next node.  

Steps:  
- Copy the value of `node.next` into `node`.  
- Set `node.next = node.next.next` to remove the next node.  

Time Complexity: O(1)  
Space Complexity: O(1)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
