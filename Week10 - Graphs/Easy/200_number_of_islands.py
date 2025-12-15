"""
Problem: Number of Islands
LeetCode #200
Difficulty: Medium
Link: https://leetcode.com/problems/number-of-islands/

Problem Statement:
Given a 2D grid of '1's (land) and '0's (water),  
return the number of islands.

An island is formed by connecting adjacent lands horizontally or vertically.

Example:
Input:
[
 ["1","1","1","1","0"],
 ["1","1","0","1","0"],
 ["1","1","0","0","0"],
 ["0","0","0","0","0"]
]
Output: 1

Approach: DFS (Depth-First Search)
----------------------------------
We scan the grid:
- When we find a '1', that means we found a NEW island.
- We perform DFS to mark all connected '1's as visited by turning them into '0'.
- Continue scanning to find more islands.

Steps:
1. Loop through every cell.
2. If grid[r][c] == '1':
      - Increment island count
      - DFS to sink the island (convert all connected '1's to '0')
3. Return total count.

Time Complexity:
- O(m × n), every cell visited at most once.

Space Complexity:
- O(m × n) recursion stack in worst case.
"""

class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            # Out of bounds or water cell → stop
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return

            # Mark current land as visited
            grid[r][c] = "0"

            # Explore all 4 directions
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        # Scan the entire grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":  # Found an unvisited island
                    count += 1
                    dfs(r, c)

        return count
