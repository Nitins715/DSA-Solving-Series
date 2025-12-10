"""
Problem: Delete Node in a BST
LeetCode #450
Difficulty: Medium
Link: https://leetcode.com/problems/delete-node-in-a-bst/

Problem Statement:
Given the root of a Binary Search Tree (BST) and a key,
delete the node with the given key and return the new root.

BST Properties:
- Left subtree < node value
- Right subtree > node value

Cases When Deleting a Node:
--------------------------------
1. Node not found → return root unchanged
2. Node is a leaf → delete directly
3. Node has ONE child → replace node with its child
4. Node has TWO children:
    - Replace node's value with its **inorder successor**
      (smallest value in right subtree)
    - Delete the successor node recursively

Approach: Recursive BST delete
------------------------------
Use recursion to search the node:
- If key < node.val → go left
- If key > node.val → go right
- If key == node.val → handle deletion cases

Time Complexity:
- O(h), where h = height of tree (O(log n) for balanced, O(n) worst case)

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
    def deleteNode(self, root, key):
        if not root:
            return None

        # Step 1: Search for the node to delete
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Step 2: Node found → handle cases

            # Case A: No left child
            if not root.left:
                return root.right

            # Case B: No right child
            if not root.right:
                return root.left

            # Case C: Two children → replace with inorder successor
            successor = root.right
            while successor.left:
                successor = successor.left

            # Copy successor's value into root
            root.val = successor.val

            # Delete the successor from right subtree
            root.right = self.deleteNode(root.right, successor.val)

        return root
