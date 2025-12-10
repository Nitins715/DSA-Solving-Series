"""
Problem: Binary Tree Preorder Traversal
LeetCode #144
Difficulty: Easy
Link: https://leetcode.com/problems/binary-tree-preorder-traversal/

Problem Statement:
Given the root of a binary tree, return its preorder traversal.
Preorder traversal visits nodes in the order:
    Node → Left → Right

Examples:
Input:
   1
    \
     2
    /
   3
Output: [1,2,3]

Input: root = []
Output: []

Approach: Recursive Preorder Traversal
--------------------------------------
Steps:
1. Visit current node
2. Traverse left subtree
3. Traverse right subtree

This is the simplest and cleanest approach.

Time Complexity:
- O(n), each node is visited exactly once.

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
    def preorderTraversal(self, root):
        res = []

        def preorder(node):
            if not node:
                return
            res.append(node.val)   # Node
            preorder(node.left)    # Left
            preorder(node.right)   # Right

        preorder(root)
        return res
