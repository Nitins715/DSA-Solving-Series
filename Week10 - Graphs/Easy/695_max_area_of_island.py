"""
Problem: Max Area of Island
LeetCode #695
Difficulty: Medium
Link: https://leetcode.com/problems/max-area-of-island/

Problem Statement:
Given a 2D grid of 0s (water) and 1s (land),  
return the **maximum area** of an island.
An island is a group of connected 1s (4-directionally).

Example:
Input:
[
 [0,0,1,0,0],
 [0,1,1,1,0],
 [0,0,1,0,0],
 [1,1,0,0,0]
]
Output: 5  (the big island)

Approach: DFS to Count Size of Each Island
------------------------------------------
We explore every island using DFS and compute its area.

Algorithm:
1. Loop through grid.
2. When you find a 1 (unvisited land):
      - Run DFS to compute its area.
      - Track max area.
3. DFS:
      - Mark cell as visited by setting it to 0.
      - Return 1 + area of 4 neighbors.

Time Complexity:
- O(m × n)

Space Complexity:
- O(m × n) recursion stack worst case.
"""

class Solution(object):
    def maxAreaOfIsland(self, grid):
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            # Out of bounds or water
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0

            # Mark as visited
            grid[r][c] = 0

            # Area = 1 + 4-direction neighbors
            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

        max_area = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))

        return max_area
