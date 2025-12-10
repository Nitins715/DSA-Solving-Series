"""
Problem: Same Tree
LeetCode #100
Difficulty: Easy
Link: https://leetcode.com/problems/same-tree/

Problem Statement:
Given the roots of two binary trees p and q, return True if the two trees are structurally identical and have the same node values.

Trees are the same if:
1. Both nodes are None → same
2. Values match AND
3. Left subtrees are same AND
4. Right subtrees are same

Examples:
Input:
p = [1,2,3], q = [1,2,3]
Output: True

Input:
p = [1,2], q = [1,None,2]
Output: False

Approach: Recursive Comparison
------------------------------
Use recursion to compare corresponding nodes in both trees.

Base Cases:
- If both nodes are None → True  
- If one is None → False  
- If values differ → False  

Otherwise, recursively compare left and right subtrees.

Time Complexity:
- O(n), must visit all nodes

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
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and \
               self.isSameTree(p.right, q.right)
