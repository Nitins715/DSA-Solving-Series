"""
Problem: Minimum Path Sum
LeetCode #64
Difficulty: Medium
Link: https://leetcode.com/problems/minimum-path-sum/

Problem Statement:
Given a m x n grid filled with non-negative numbers,
find a path from top-left to bottom-right which minimizes
the sum of all numbers along its path.

You can only move either down or right at any point in time.

Examples:
Input: grid = [[1,3,1],
               [1,5,1],
               [4,2,1]]
Output: 7
Explanation:
Path: 1 → 3 → 1 → 1 → 1

Input: grid = [[1,2,3],
               [4,5,6]]
Output: 12

Key Insight:
This is a **Dynamic Programming** problem.

To reach cell (i, j), you can come only from:
- cell above (i-1, j)
- cell to the left (i, j-1)

Approach: Dynamic Programming (In-Place Optimization)
-----------------------------------------------------
Steps:
1. Initialize the first row by accumulating sums from left to right.
2. Initialize the first column by accumulating sums from top to bottom.
3. For each remaining cell:
   - grid[i][j] += min(grid[i-1][j], grid[i][j-1])
4. The bottom-right cell contains the minimum path sum.

Time Complexity:
- O(m × n)

Space Complexity:
- O(1) (in-place modification)
"""

class Solution(object):
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])

        # Initialize first row
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]

        # Initialize first column
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]

        # Fill the rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[m - 1][n - 1]
