"""
Problem: Populating Next Right Pointers in Each Node
LeetCode #116
Difficulty: Medium
Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

Problem Statement:
You are given a **perfect binary tree** (every level is full).
Fill each node's `next` pointer so it points to its immediate right neighbor.
If there is no right neighbor, set `next = None`.

Example:
Input:
      1
    /   \
   2     3
  / \   / \
 4  5  6   7

Output:
1→None  
2→3→None  
4→5→6→7→None  

Approach: Using Already Established Next Pointers (O(1) Space)
--------------------------------------------------------------
Since the tree is **perfect**, we can use the fact that:
- `left.next = right`
- `right.next = node.next.left` (if node.next exists)

We iterate level by level WITHOUT extra space.

Steps:
1. Start from the leftmost node of each level.
2. Connect its left and right child.
3. Connect right child to next.left if next exists.
4. Move horizontally using next pointers.

Why this works:
In a perfect tree, children exist in predictable positions, allowing O(1) traversal.

Time Complexity:
- O(n), touch each node once.

Space Complexity:
- O(1), no queue or recursion needed.
"""

# Definition for a Node.
# class Node(object):
#     def __init__(self, val=0, left=None, right=None, next=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next

class Solution(object):
    def connect(self, root):
        if not root:
            return root

        leftmost = root

        # Iterate over levels
        while leftmost.left:
            head = leftmost

            while head:
                # Connect left child to right child
                head.left.next = head.right

                # Connect right child to next subtree's left child
                if head.next:
                    head.right.next = head.next.left

                head = head.next  # Move horizontally

            leftmost = leftmost.left  # Move down to next level

        return root
