"""
Problem: Word Search
LeetCode #79
Difficulty: Medium
Link: https://leetcode.com/problems/word-search/

Problem Statement:
Given an m x n grid of characters board and a string word,
return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.

The same letter cell **may not be used more than once**.

Examples:
Input: board = 
[["A","B","C","E"],
 ["S","F","C","S"],
 ["A","D","E","E"]], word = "ABCCED"
Output: true

Input: board = 
[["A","B","C","E"],
 ["S","F","C","S"],
 ["A","D","E","E"]], word = "SEE"
Output: true

Input: board = 
[["A","B","C","E"],
 ["S","F","C","S"],
 ["A","D","E","E"]], word = "ABCB"
Output: false

Approach:
- Use **DFS + backtracking**.
- For each cell in the grid:
  - If the character matches word[0], start a DFS search.
- In DFS:
  - If index == len(word), we found the entire word → return True.
  - Check boundaries and matching characters.
  - Mark the cell as visited by temporarily replacing it with a special marker (e.g., '#').
  - Explore all 4 directions.
  - Backtrack by restoring the character.
- If none of the paths match, return False.

Time Complexity: O(m * n * 4^len(word))
Space Complexity: O(len(word)) recursion depth
"""

class Solution(object):
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            # Reached end of word
            if i == len(word):
                return True

            # Out of bounds OR mismatch
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
                return False

            # Mark current cell as visited
            temp = board[r][c]
            board[r][c] = "#"

            # Explore all 4 directions
            found = (dfs(r + 1, c, i + 1) or
                     dfs(r - 1, c, i + 1) or
                     dfs(r, c + 1, i + 1) or
                     dfs(r, c - 1, i + 1))

            # Backtrack
            board[r][c] = temp

            return found

        # Start DFS from every cell
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False
