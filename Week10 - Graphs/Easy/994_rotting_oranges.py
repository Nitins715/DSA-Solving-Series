"""
Problem: Rotting Oranges
LeetCode #994
Difficulty: Medium
Link: https://leetcode.com/problems/rotting-oranges/

Problem Statement:
You are given a grid where:
- 0 → empty cell
- 1 → fresh orange
- 2 → rotten orange

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes needed to rot all fresh oranges.
If it is impossible, return -1.

Examples:
Input:
grid = [[2,1,1],
        [1,1,0],
        [0,1,1]]
Output: 4

Input:
grid = [[2,1,1],
        [0,1,1],
        [1,0,1]]
Output: -1

Approach: Multi-Source BFS
--------------------------
- All initially rotten oranges are sources (start points).
- Each BFS level represents 1 minute.
- Count fresh oranges and decrease as they rot.
- If fresh oranges remain at the end → return -1.

Algorithm:
1. Add all rotten oranges to the queue.
2. Count fresh oranges.
3. Perform BFS layer by layer.
4. Track minutes.
5. If fresh count > 0 → impossible.

Time Complexity:
- O(m × n)

Space Complexity:
- O(m × n) for queue.
"""

from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        # Step 1: Initialize
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # Step 2: BFS
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))

            minutes += 1

        return minutes if fresh == 0 else -1
