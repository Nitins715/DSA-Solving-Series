"""
Problem: Path Sum
LeetCode #112
Difficulty: Easy
Link: https://leetcode.com/problems/path-sum/

Problem Statement:
Given the root of a binary tree and an integer targetSum, return True if the tree has a root-to-leaf path such that the sum of node values equals targetSum.

A leaf is a node with no children.

Examples:
Input: root = [5,4,8,11,None,13,4,7,2,None,None,None,1], targetSum = 22
Output: True  
Path: 5 → 4 → 11 → 2

Input: root = [1,2,3], targetSum = 5
Output: False

Approach: DFS (Recursive)
-------------------------
At each node:
- Subtract node.val from targetSum.
- If it's a leaf AND remaining sum == 0 → return True.
- Recursively check left and right subtrees.

Why this works:
We explore every root-to-leaf path and check if any matches targetSum.

Time Complexity:
- O(n), visit every node once.

Space Complexity:
- O(h), recursion stack.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        # Subtract current node value from remaining sum
        targetSum -= root.val

        # If it's a leaf node, check if remaining sum is 0
        if not root.left and not root.right:
            return targetSum == 0

        # Otherwise continue exploring
        return self.hasPathSum(root.left, targetSum) or \
               self.hasPathSum(root.right, targetSum)
