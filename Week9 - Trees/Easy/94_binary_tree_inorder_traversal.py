"""
Problem: Binary Tree Inorder Traversal
LeetCode #94
Difficulty: Easy
Link: https://leetcode.com/problems/binary-tree-inorder-traversal/

Problem Statement:
Given the root of a binary tree, return its inorder traversal.
Inorder traversal visits nodes in the order:
    Left → Node → Right

Examples:
Input:
   1
    \
     2
    /
   3
Output: [1,3,2]

Input: root = []
Output: []

Approach: Recursive Inorder Traversal
-------------------------------------
Steps:
1. Traverse left subtree
2. Visit current node
3. Traverse right subtree

This is the simplest and most readable approach.

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
    def inorderTraversal(self, root):
        res = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        inorder(root)
        return res
