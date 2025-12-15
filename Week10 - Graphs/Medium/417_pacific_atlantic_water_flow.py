"""
Problem: Pacific Atlantic Water Flow
LeetCode #417
Difficulty: Medium
Link: https://leetcode.com/problems/pacific-atlantic-water-flow/

Problem Statement:
You are given an m x n matrix heights where heights[r][c] represents
the height of a cell.

Water can flow from a cell to another cell if:
- The next cell is in one of 4 directions (up, down, left, right)
- The next cell's height is less than or equal to the current cell's height

The Pacific Ocean touches:
- Top row and left column

The Atlantic Ocean touches:
- Bottom row and right column

Return a list of coordinates where water can flow to **both oceans**.

Example:
Input:
heights =
[
 [1,2,2,3,5],
 [3,2,3,4,4],
 [2,4,5,3,1],
 [6,7,1,4,5],
 [5,1,1,2,4]
]
Output:
[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Approach: Reverse DFS (Multi-source DFS)
----------------------------------------
Instead of flowing water from every cell to the oceans,
we reverse the thinking:

- Start DFS from the **Pacific borders** and mark all cells that can
  reach the Pacific.
- Start DFS from the **Atlantic borders** and mark all cells that can
  reach the Atlantic.
- A cell that is reachable in both searches can flow to both oceans.

DFS Rule (Reversed):
- From current cell, you can go to a neighbor if
      neighbor_height >= current_height

Why this works:
- Reversing the flow avoids redundant DFS from each cell.
- Each cell is visited at most twice.

Time Complexity:
- O(m × n)

Space Complexity:
- O(m × n) for visited sets + recursion stack
"""

class Solution(object):
    def pacificAtlantic(self, heights):
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            visited.add((r, c))
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols and
                    (nr, nc) not in visited and
                    heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, visited)

        # Pacific borders (top row, left column)
        for c in range(cols):
            dfs(0, c, pacific)
        for r in range(rows):
            dfs(r, 0, pacific)

        # Atlantic borders (bottom row, right column)
        for c in range(cols):
            dfs(rows - 1, c, atlantic)
        for r in range(rows):
            dfs(r, cols - 1, atlantic)

        # Cells reachable by both oceans
        return list(pacific & atlantic)
