"""
Problem: Shortest Path in Binary Matrix
LeetCode #1091
Difficulty: Medium
Link: https://leetcode.com/problems/shortest-path-in-binary-matrix/

Problem Statement:
Given an n x n binary matrix grid, return the length of the shortest clear path
from the top-left cell (0,0) to the bottom-right cell (n-1,n-1).

Rules:
- You can move in **8 directions** (horizontal, vertical, diagonal).
- A cell is clear if its value is 0.
- You can only pass through clear cells.
- If there is no clear path, return -1.

Examples:
Input:
grid = [[0,1],
        [1,0]]
Output: 2

Input:
grid = [[0,0,0],
        [1,1,0],
        [1,1,0]]
Output: 4

Input:
grid = [[1,0],
        [0,0]]
Output: -1

Approach: BFS (Shortest Path in Unweighted Graph)
-------------------------------------------------
- Treat each cell as a node in a graph.
- Since all moves have equal cost (1), **BFS guarantees the shortest path**.
- Start BFS from (0,0).
- Each BFS layer represents path length +1.
- Stop when we reach (n-1, n-1).

Steps:
1. If start or end cell is blocked → return -1.
2. Use a queue storing (row, col, distance).
3. Mark visited cells to avoid revisiting.
4. Explore all 8 directions.
5. Return distance when destination is reached.

Time Complexity:
- O(n²), each cell visited once.

Space Complexity:
- O(n²), queue + visited.
"""

from collections import deque

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)

        # If start or end is blocked
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1

        # 8 possible directions
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]

        queue = deque([(0, 0, 1)])  # (row, col, path_length)
        grid[0][0] = 1  # mark visited

        while queue:
            r, c, dist = queue.popleft()

            # Reached destination
            if r == n - 1 and c == n - 1:
                return dist

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1  # mark visited
                    queue.append((nr, nc, dist + 1))

        return -1
