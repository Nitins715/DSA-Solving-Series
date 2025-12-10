"""
Problem: Binary Tree Postorder Traversal
LeetCode #145
Difficulty: Easy
Link: https://leetcode.com/problems/binary-tree-postorder-traversal/

Problem Statement:
Given the root of a binary tree, return its postorder traversal.
Postorder traversal visits nodes in the order:
    Left → Right → Node

Examples:
Input:
   1
    \
     2
    /
   3
Output: [3,2,1]

Input: root = []
Output: []

Approach: Recursive Postorder Traversal
---------------------------------------
Steps:
1. Traverse left subtree
2. Traverse right subtree
3. Visit current node

This is the simplest and cleanest way to implement postorder.

Time Complexity:
- O(n), each node is visited once.

Space Complexity:
- O(h), where h is the height of the tree (recursion stack).
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        res = []

        def postorder(node):
            if not node:
                return
            postorder(node.left)   # Left
            postorder(node.right)  # Right
            res.append(node.val)   # Node

        postorder(root)
        return res
