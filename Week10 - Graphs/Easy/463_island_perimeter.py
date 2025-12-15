"""
Problem: Island Perimeter
LeetCode #463
Difficulty: Easy
Link: https://leetcode.com/problems/island-perimeter/

Problem Statement:
You are given a grid where:
- 1 represents land
- 0 represents water

There is exactly **one island** (one connected component of land).
Return the *perimeter* of that island.

Example:
Input:
[
 [0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]
]
Output: 16

Approach: Count Edges
---------------------
For each land cell:
- Add 4 to the perimeter.
- Subtract 1 for every adjacent land cell (up, down, left, right).

Because adjacent land cells share edges → each shared edge removes 2 from the total (1 for each direction).

Algorithm:
1. Loop through grid.
2. For each land cell:
    +4 to perimeter
    If land above → -2
    If land left  → -2

Why only check top and left?
- To avoid double counting. Each shared edge is handled once.

Time Complexity:
- O(m × n)

Space Complexity:
- O(1)
"""

class Solution(object):
    def islandPerimeter(self, grid):
        rows, cols = len(grid), len(grid[0])
        perimeter = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # Add 4 for each land cell
                    perimeter += 4

                    # Subtract edges shared with the above cell
                    if r > 0 and grid[r-1][c] == 1:
                        perimeter -= 2

                    # Subtract edges shared with the left cell
                    if c > 0 and grid[r][c-1] == 1:
                        perimeter -= 2

        return perimeter
