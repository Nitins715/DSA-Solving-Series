"""
Problem: Symmetric Tree
LeetCode #101
Difficulty: Easy
Link: https://leetcode.com/problems/symmetric-tree/

Problem Statement:
Given the root of a binary tree, return True if the tree is symmetric (a mirror of itself).

A tree is symmetric if:
- Left subtree is a mirror of the right subtree.

Example:
Input: [1,2,2,3,4,4,3]
Output: True

Input: [1,2,2,None,3,None,3]
Output: False

Approach: Recursive Mirror Check
--------------------------------
Two subtrees are mirror images if:
1. Their roots have the same value.
2. The left subtree of one is a mirror of the right subtree of the other.
3. The right subtree of one is a mirror of the left subtree of the other.

Define a helper function `isMirror(left, right)`:
- If both nodes are None → symmetric
- If only one is None → not symmetric
- Check values and recursively check outer & inner children

Time Complexity:
- O(n), every node visited once

Space Complexity:
- O(h), recursion stack where h = tree height
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True

        def isMirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False

            return isMirror(left.left, right.right) and \
                   isMirror(left.right, right.left)

        return isMirror(root.left, root.right)
