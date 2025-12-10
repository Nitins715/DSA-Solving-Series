"""
Problem: Validate Binary Search Tree
LeetCode #98
Difficulty: Medium
Link: https://leetcode.com/problems/validate-binary-search-tree/

Problem Statement:
Given the root of a binary tree, determine if it is a valid Binary Search Tree (BST).

Rules of a BST:
- Left subtree contains only nodes with values < root.val
- Right subtree contains only nodes with values > root.val
- Both left and right subtrees must also be valid BSTs

Examples:
Input: [2,1,3] → True  
Input: [5,1,4,None,None,3,6] → False (because 3 is in the wrong position)

Approach: DFS with Value Bounds
--------------------------------
Each node must satisfy a valid range:
- root starts with (-∞, +∞)
- Left child must be in (min, root.val)
- Right child must be in (root.val, max)

Recursive function:
validate(node, low, high):
    - If node is None → True
    - If node.val <= low or >= high → False
    - Validate left with (low, node.val)
    - Validate right with (node.val, high)

Why this works:
We ensure BST validity not only locally but across the entire path from root.

Time Complexity:
- O(n), visit each node once

Space Complexity:
- O(h), recursion stack
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isValidBST(self, root):
        def validate(node, low, high):
            if not node:
                return True

            if not (low < node.val < high):
                return False

            return validate(node.left, low, node.val) and \
                   validate(node.right, node.val, high)

        return validate(root, float("-inf"), float("inf"))
