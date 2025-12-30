# File Name: 221_maximal_square.py

"""
Problem: Maximal Square
LeetCode #221
Difficulty: Medium
Link: https://leetcode.com/problems/maximal-square/

Problem Statement:
Given an m x n binary matrix filled with '0's and '1's,
find the largest square containing only '1's and return its area.

Examples:
Input:
matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 4
Explanation:
The largest square has side length 2 → area = 4

Input:
matrix = [["0","1"],["1","0"]]
Output: 1

Key Insight:
This is a **Dynamic Programming** problem.

Let dp[i][j] represent the side length of the largest square
ending at cell (i, j) (bottom-right corner).

Approach: Dynamic Programming
-----------------------------
Steps:
1. Create a DP table of size (m+1) x (n+1) initialized with 0s.
   (Extra row and column simplify boundary checks.)
2. Iterate through the matrix:
   - If matrix[i-1][j-1] == '1':
       dp[i][j] = 1 + min(
           dp[i-1][j],     # top
           dp[i][j-1],     # left
           dp[i-1][j-1]    # top-left
       )
3. Track the maximum side length found.
4. Return (max_side_length)² as the area.

Time Complexity:
- O(m × n)

Space Complexity:
- O(m × n)
"""

class Solution(object):
    def maximalSquare(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_side = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],
                        dp[i][j - 1],
                        dp[i - 1][j - 1]
                    )
                    max_side = max(max_side, dp[i][j])

        return max_side * max_side
