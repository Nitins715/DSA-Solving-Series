"""
Problem: Flood Fill
LeetCode #733
Difficulty: Easy
Link: https://leetcode.com/problems/flood-fill/

Problem Statement:
You are given an image represented by a 2D grid.
Given a starting pixel (sr, sc) and a newColor,  
recolor the entire connected component of the starting pixel  
(connected 4-directionally: up, down, left, right).

Example:
Input:
image = [[1,1,1],
         [1,1,0],
         [1,0,1]]
sr = 1, sc = 1, newColor = 2

Output:
[[2,2,2],
 [2,2,0],
 [2,0,1]]

Approach: DFS (Depth-First Search)
----------------------------------
1. Store the original color at (sr, sc).
2. If original color == newColor → no changes required.
3. Use DFS to recolor:
    - Recolor current pixel
    - Recurse to its 4 neighbors that match original color

Time Complexity:
- O(m × n), each cell visited at most once.

Space Complexity:
- O(m × n) worst-case recursion stack (for large fill regions).
"""

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        rows, cols = len(image), len(image[0])
        original = image[sr][sc]

        # If the color is already the target, no need to fill
        if original == newColor:
            return image

        def dfs(r, c):
            # Boundary + original color check
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            if image[r][c] != original:
                return

            # Recolor current pixel
            image[r][c] = newColor

            # Explore 4 neighbors
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        dfs(sr, sc)
        return image
