"""
Problem: Unique Paths II
LeetCode #63
Difficulty: Medium
Link: https://leetcode.com/problems/unique-paths-ii/

Problem Statement:
A robot is located at the top-left corner of a m x n grid.
Some cells in the grid are marked as obstacles.

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid.

Return the number of unique paths to reach the bottom-right corner.
If an obstacle is present at the start or end cell, return 0.

Examples:
Input:
obstacleGrid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2

Input:
obstacleGrid = [
  [1,0]
]
Output: 0

Key Insight:
This is a **Dynamic Programming** problem with blocked cells.

Each cell's number of ways depends on:
- the cell above
- the cell to the left

If a cell contains an obstacle, it contributes 0 paths.

Approach: Dynamic Programming (In-Place Optimization)
-----------------------------------------------------
Steps:
1. If the start cell has an obstacle → return 0.
2. Initialize the starting cell as 1.
3. Iterate through the grid:
   - If obstacleGrid[i][j] == 1:
       set obstacleGrid[i][j] = 0
   - Else:
       obstacleGrid[i][j] = paths from top + paths from left
4. Return the value at bottom-right cell.

Time Complexity:
- O(m × n)

Space Complexity:
- O(1) (in-place modification)
"""

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        obstacleGrid[0][0] = 1

        # Initialize first row
        for j in range(1, n):
            obstacleGrid[0][j] = 0 if obstacleGrid[0][j] == 1 else obstacleGrid[0][j - 1]

        # Initialize first column
        for i in range(1, m):
            obstacleGrid[i][0] = 0 if obstacleGrid[i][0] == 1 else obstacleGrid[i - 1][0]

        # Fill the rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]

        return obstacleGrid[m - 1][n - 1]
