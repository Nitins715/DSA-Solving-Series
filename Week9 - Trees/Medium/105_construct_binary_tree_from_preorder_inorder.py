"""
Problem: Construct Binary Tree from Preorder and Inorder Traversal
LeetCode #105
Difficulty: Medium
Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Problem Statement:
Given two integer arrays:
- preorder: Node → Left → Right
- inorder:  Left → Node → Right

Construct the binary tree and return its root.

Example:
preorder = [3,9,20,15,7]
inorder  = [9,3,15,20,7]

Tree:
      3
     / \
    9   20
       /  \
      15   7

Approach: Recursive Tree Reconstruction
---------------------------------------
Key Insight:
- The first element of preorder is ALWAYS the root.
- Find that root in inorder → splits left & right subtrees.

Steps:
1. Preorder: pick root from the front.
2. In inorder array:
      left of root → left subtree
      right of root → right subtree
3. Recursively build left and right subtrees.

Optimization:
- Use a hashmap to store inorder indices → O(1) lookup.

Time Complexity:
- O(n), each node handled once.

Space Complexity:
- O(n), map + recursion stack.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        # Map values → inorder indices for quick lookup
        index_map = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0  # pointer in preorder list

        def build(left, right):
            if left > right:
                return None

            # Take next element in preorder as root
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1

            root = TreeNode(root_val)

            # Build left & right subtrees using inorder boundaries
            mid = index_map[root_val]
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)
