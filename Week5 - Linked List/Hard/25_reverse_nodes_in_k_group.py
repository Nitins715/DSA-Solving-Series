"""
Problem: Reverse Nodes in k-Group  
LeetCode #25  
Difficulty: Hard  
Link: https://leetcode.com/problems/reverse-nodes-in-k-group/  

Problem Statement:  
Given the head of a linked list, reverse the nodes of the list k at a time,  
and return the modified list.  
k is a positive integer and is less than or equal to the length of the list.  
If the number of nodes is not a multiple of k, leave the last nodes as they are.  

You may not alter the values in the list's nodes — only nodes themselves may be changed.

Examples:  
Input: head = [1,2,3,4,5], k = 2  
Output: [2,1,4,3,5]  

Input: head = [1,2,3,4,5], k = 3  
Output: [3,2,1,4,5]  

Approach (Iterative + In-place Reverse):  
1. Use a dummy node to handle edge cases.  
2. Use two pointers (`group_prev`, `kth`) to identify groups of size k.  
3. Reverse each group of k nodes in place using pointer manipulation.  
4. Connect the reversed group to the rest of the list.  
5. Continue until fewer than k nodes remain.

Helper Function:  
- `getKth(curr, k)` → returns the k-th node from curr or None if fewer than k remain.  

Time Complexity: O(n)  
Space Complexity: O(1)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        def getKth(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr

        while True:
            kth = getKth(group_prev, k)
            if not kth:
                break

            group_next = kth.next

            # Reverse the group
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp

        return dummy.next
