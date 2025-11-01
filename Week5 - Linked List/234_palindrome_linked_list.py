"""
Problem: Palindrome Linked List  
LeetCode #234  
Difficulty: Easy  
Link: https://leetcode.com/problems/palindrome-linked-list/  

Problem Statement:  
Given the head of a singly linked list, return true if it is a palindrome, or false otherwise.  

Examples:  
Input: head = [1,2,2,1]  
Output: true  

Input: head = [1,2]  
Output: false  

Approach (Fast-Slow + Reverse Second Half):  
1. Use fast and slow pointers to find the middle of the linked list.  
2. Reverse the second half of the list.  
3. Compare nodes from the first half and the reversed second half.  
4. If all match, it's a palindrome; otherwise, not.  

Steps:  
- Use fast/slow to find mid.  
- Reverse from `slow` onward.  
- Compare from `head` and `reversed_head`.  
- (Optional) Restore the list to original if needed.  

Time Complexity: O(n)  
Space Complexity: O(1)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        # Step 1: Find middle (slow will point to mid)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        # Step 3: Compare first and second halves
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
