"""
Problem: Unique Paths
LeetCode #62
Difficulty: Medium
Link: https://leetcode.com/problems/unique-paths/

Problem Statement:
A robot is located at the top-left corner of an m x n grid.
The robot can only move either down or right at any point in time.

The robot is trying to reach the bottom-right corner of the grid.
How many possible unique paths are there?

Examples:
Input: m = 3, n = 7
Output: 28

Input: m = 3, n = 2
Output: 3

Key Insight:
This is a **Dynamic Programming** problem.

To reach any cell (i, j), the robot can only come from:
- the cell above (i - 1, j)
- the cell to the left (i, j - 1)

Approach: Dynamic Programming
-----------------------------
Let dp[i][j] be the number of unique paths to reach cell (i, j).

Steps:
1. Initialize a DP table of size m x n.
2. Set dp[i][0] = 1 for all i (only one way to move down).
3. Set dp[0][j] = 1 for all j (only one way to move right).
4. For each cell (i, j):
   - dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
5. Return dp[m - 1][n - 1].

Time Complexity:
- O(m × n)

Space Complexity:
- O(m × n)
"""

class Solution(object):
    def uniquePaths(self, m, n):
        dp = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]
