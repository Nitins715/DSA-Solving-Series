"""
Problem: Lowest Common Ancestor of a Binary Tree
LeetCode #236
Difficulty: Medium
Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Problem Statement:
Given a binary tree and two nodes p and q, return their Lowest Common Ancestor (LCA).
The LCA is the lowest node in the tree that has both p and q as descendants 
(allowing a node to be a descendant of itself).

Examples:
Input:
      3
     / \
    5   1
   / \  / \
  6  2 0  8
    / \
   7   4
p = 5, q = 1 → Output: 3  
p = 5, q = 4 → Output: 5 (because a node can be its own ancestor)

Approach: DFS (Postorder)
-------------------------
We use recursion to explore the whole tree.

Logic:
1. If root is None → return None  
2. If root == p or root == q → return root  
3. Recursively search left and right subtrees:
      left = LCA in left subtree
      right = LCA in right subtree
4. If both left and right are non-null → root is the LCA  
5. If only one side is non-null → return that side  
6. If both are None → return None

Why this works:
- LCA is found when p and q split into different branches.
- If both are found deeper on one side, propagate upward.

Time Complexity:
- O(n), visit every node

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
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both sides returned a node, current node is LCA
        if left and right:
            return root

        # Otherwise propagate the non-null return
        return left if left else right
