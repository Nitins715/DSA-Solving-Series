"""
Problem: Binary Tree Maximum Path Sum
LeetCode #124
Difficulty: Hard
Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/

Problem Statement:
Given the root of a binary tree, return the maximum path sum.
A path may start and end at ANY node.
A path can go through parent-child connections only.

A valid path can:
- Go left → node → right
- Or just be a single node
- Or extend one side upward

Examples:
Input: [1,2,3]
Paths: 2→1→3 has sum 6
Output: 6

Input: [-10,9,20,None,None,15,7]
Max path: 15 → 20 → 7 = 42
Output: 42

Approach: DFS + Return "Max Gain"
----------------------------------
For each node, we compute:

1. **Left Gain**: max sum from left subtree (ignore negatives → max(0, left))
2. **Right Gain**: max sum from right subtree (ignore negatives → max(0, right))
3. **Path Through Node**:
        node.val + left_gain + right_gain
   This may be the **maximum path** including both children.

We keep a global max to track the best sum seen so far.

Return to parent:
- max gain contributed upward:
        node.val + max(left_gain, right_gain)

Why ignore negative gains?
- Adding a negative path only reduces total sum.

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
    def maxPathSum(self, root):
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            # Max gain from left and right (ignore negatives)
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            # Path through current node using BOTH children
            current_path_sum = node.val + left_gain + right_gain

            # Update global max path sum
            self.max_sum = max(self.max_sum, current_path_sum)

            # Return the max gain to parent (only one side allowed)
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.max_sum
