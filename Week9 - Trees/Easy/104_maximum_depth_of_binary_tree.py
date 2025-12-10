"""
Problem: Maximum Depth of Binary Tree
LeetCode #104
Difficulty: Easy
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

Problem Statement:
Given the root of a binary tree, return its maximum depth.
Maximum depth = number of nodes along the longest path from root → leaf.

Examples:
Input: [3,9,20,None,None,15,7]
Output: 3

Input: root = []
Output: 0

Approach: Recursive Depth Calculation
-------------------------------------
For any node:
- Max depth = 1 + max(depth(left), depth(right))
- If the node is None → depth = 0

This naturally fits recursion.

Time Complexity:
- O(n), visit each node once

Space Complexity:
- O(h), recursion stack where h = height of tree (worst-case O(n), best-case O(log n))
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
