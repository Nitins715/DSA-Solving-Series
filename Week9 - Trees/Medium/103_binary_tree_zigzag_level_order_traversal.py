"""
Problem: Binary Tree Zigzag Level Order Traversal
LeetCode #103
Difficulty: Medium
Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Problem Statement:
Given the root of a binary tree, return the zigzag level order traversal:
- Level 1 → Left to Right
- Level 2 → Right to Left
- Level 3 → Left to Right
- and so on...

Example:
Input:
    3
   / \
  9  20
     / \
    15  7

Output:
[[3], [20,9], [15,7]]

Approach: BFS with Direction Toggle
-----------------------------------
Use a queue for level order traversal.  
For each level:
1. Extract all nodes in the level.
2. If direction = left→right → append normally.
3. If direction = right→left → append reversed.
4. Flip direction for next level.

Time Complexity:
- O(n), visit all nodes.

Space Complexity:
- O(n), queue + result storage.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        result = []
        queue = deque([root])
        left_to_right = True

        while queue:
            size = len(queue)
            level = []

            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Reverse if needed
            if not left_to_right:
                level.reverse()

            result.append(level)
            left_to_right = not left_to_right  # Toggle direction

        return result
