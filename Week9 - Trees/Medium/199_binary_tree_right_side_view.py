"""
Problem: Binary Tree Right Side View
LeetCode #199
Difficulty: Medium
Link: https://leetcode.com/problems/binary-tree-right-side-view/

Problem Statement:
Given the root of a binary tree, return the values of the nodes you can see from the **right side**.

Right side view means:
For each level of the tree, the visible node is the **rightmost node**.

Examples:
Input:
    1
   / \
  2   3
   \   \
    5   4
Output: [1,3,4]

Input: root = []
Output: []

Approach: BFS (Level Order) — Take Last Node of Each Level
-----------------------------------------------------------
- Traverse the tree level by level using a queue.
- For each level, the rightmost element (last in the queue for that level) is visible.
- Append it to the result.

Alternative: DFS (Right-first pre-order), but BFS is simpler.

Time Complexity:
- O(n), visit all nodes.

Space Complexity:
- O(n), queue storage.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            size = len(queue)

            for i in range(size):
                node = queue.popleft()

                # If it's the last node of this level → rightmost
                if i == size - 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
