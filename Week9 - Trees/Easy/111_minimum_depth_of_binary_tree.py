"""
Problem: Minimum Depth of Binary Tree
LeetCode #111
Difficulty: Easy
Link: https://leetcode.com/problems/minimum-depth-of-binary-tree/

Problem Statement:
Given the root of a binary tree, return its minimum depth.
Minimum depth = the number of nodes along the shortest path from the root node down to the nearest leaf node.

Important:
A leaf is a node with **no left and no right child**.

Examples:
Input: [3,9,20,None,None,15,7]
Output: 2  (path: 3 → 9)

Input: root = []
Output: 0

Approach: BFS (Fastest for Minimum Depth)
-----------------------------------------
We use BFS because:
- It finds the first leaf at the shallowest level.
- As soon as a leaf is found, we return the depth.

Steps:
1. If root is null → return 0.
2. Use a queue for BFS.
3. Track depth level-by-level.
4. When a leaf node is found → return depth immediately.

Time Complexity:
- O(n), but often stops early.

Space Complexity:
- O(n), queue usage.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0

        queue = deque([(root, 1)])

        while queue:
            node, depth = queue.popleft()

            # Check if this is a leaf
            if not node.left and not node.right:
                return depth

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
