"""
Problem: Copy List with Random Pointer  
LeetCode #138  
Difficulty: Medium  
Link: https://leetcode.com/problems/copy-list-with-random-pointer/  

Problem Statement:  
A linked list is given such that each node contains an additional random pointer  
which could point to any node in the list or null.  

Return a deep copy of the list (new nodes, no shared references).  

Examples:  
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]  
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]  

Approach (Optimized — O(1) Space, O(n) Time):  
1. **Interweaving Step:**  
   - For each original node, insert its copy just after it.  
   - Example: A → B → C becomes A → A' → B → B' → C → C'.  

2. **Assign Random Pointers:**  
   - For each original node, set `copy.random = node.random.next` (if random exists).  

3. **Separate the Lists:**  
   - Restore original list and extract the copied list simultaneously.  

This approach avoids using extra space like a hashmap while maintaining linear time complexity.

Time Complexity: O(n)  
Space Complexity: O(1)
"""

# Definition for a Node.
class Node:
    def __init__(self, val: int, next: 'Node' = None, random: 'Node' = None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        # Step 1: Interweave cloned nodes with original nodes
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next

        # Step 2: Assign random pointers for cloned nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: Separate original and copied lists
        curr = head
        copy_head = head.next
        copy_curr = copy_head

        while curr:
            curr.next = curr.next.next
            if copy_curr.next:
                copy_curr.next = copy_curr.next.next
            curr = curr.next
            copy_curr = copy_curr.next

        return copy_head
