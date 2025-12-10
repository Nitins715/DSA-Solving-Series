"""
Problem: Construct Binary Tree from Inorder and Postorder Traversal
LeetCode #106
Difficulty: Medium
Link: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

Given two integer arrays:
- inorder:   Left → Node → Right
- postorder: Left → Right → Node  (last element = root)

Construct the binary tree and return its root.

Example:
inorder   = [9,3,15,20,7]
postorder = [9,15,7,20,3]

Tree:
      3
     / \
    9   20
       /  \
      15   7

Approach: Recursive Construction Using Postorder
------------------------------------------------
Key Insight:
- The **last** element in postorder is ALWAYS the root.
- Find that root in inorder → splits left & right subtree.
- Important:
    Build **right subtree first**, then left (because postorder processes right before left if we iterate backwards).

Steps:
1. Use a hash map to store inorder indices for O(1) lookup.
2. Use a pointer (post_idx) starting from the end of postorder.
3. Recursively build tree:
      - root = postorder[post_idx]
      - split inorder into left and right using root index
      - build right subtree
      - build left subtree

Time Complexity:
- O(n), each element used once.

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
    def buildTree(self, inorder, postorder):
        # Map values to their indices in inorder for fast lookup
        index_map = {val: i for i, val in enumerate(inorder)}
        self.post_idx = len(postorder) - 1

        def build(left, right):
            if left > right:
                return None

            # Step 1: Create root from postorder
            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            root = TreeNode(root_val)

            # Step 2: Find inorder index
            mid = index_map[root_val]

            # Step 3: Build right subtree FIRST, then left
            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)

            return root

        return build(0, len(inorder) - 1)
