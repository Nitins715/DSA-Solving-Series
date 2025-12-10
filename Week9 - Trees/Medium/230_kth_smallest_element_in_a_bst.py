"""
Problem: Kth Smallest Element in a BST
LeetCode #230
Difficulty: Medium
Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Problem Statement:
Given the root of a Binary Search Tree (BST) and an integer k,
return the k-th smallest element in the tree.

BST property:
Inorder traversal of a BST produces a sorted list.

Examples:
Input: root = [3,1,4,null,2], k = 1 → Output: 1  
Input: root = [5,3,6,2,4,null,null,1], k = 3 → Output: 3

Approach: Inorder Traversal (Optimal)
-------------------------------------
- Perform **inorder DFS** (Left → Node → Right).
- Count nodes as you visit them.
- When the count hits k → return that node’s value.

Time Complexity:
- O(k) on average (stop once kth element found)
- Worst case O(n)

Space Complexity:
- O(h) recursion stack, where h = height of tree
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        self.count = 0
        self.ans = None

        def inorder(node):
            if not node or self.ans is not None:
                return

            inorder(node.left)

            self.count += 1
            if self.count == k:
                self.ans = node.val
                return

            inorder(node.right)

        inorder(root)
        return self.ans
