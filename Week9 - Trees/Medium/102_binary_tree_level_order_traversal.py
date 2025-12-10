"""
Problem: Binary Tree Level Order Traversal
LeetCode #102
Difficulty: Medium
Link: https://leetcode.com/problems/binary-tree-level-order-traversal/

Problem Statement:
Given the root of a binary tree, return its level order traversal 
(also known as Breadth-First Search, BFS):
Visit nodes level by level from left to right.

Example:
Input:
    3
   / \
  9  20
     / \
    15  7

Output:
[[9,3,20,15,7]] → Actually grouped by levels → [[3],[9,20],[15,7]]

Input: root = []
Output: []

Approach: BFS Using a Queue
---------------------------
- Use a queue to process nodes level by level.
- For each level:
    1. Count number of nodes in the current level (queue size)
    2. Pop that many nodes
    3. Add their children to queue
    4. Append values to result for that level

Time Complexity:
- O(n), visit each node once.

Space Complexity:
- O(n), queue stores nodes by level.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level = []
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result
