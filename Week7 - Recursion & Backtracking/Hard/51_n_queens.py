"""
Problem: N-Queens
LeetCode #51
Difficulty: Hard
Link: https://leetcode.com/problems/n-queens/

Problem Statement:
The n-queens puzzle is the problem of placing n queens on an nxn chessboard
such that no two queens attack each other.

Return all distinct solutions to the n-queens puzzle.
Each solution contains an arrangement where:
- No queens share the same row
- No queens share the same column
- No queens share the same diagonal

Represent each solution as a list of strings, where:
'.' → empty
'Q' → queen

Examples:
Input: n = 4
Output:
[
 [".Q..",
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",
  "Q...",
  "...Q",
  ".Q.."]
]

Approach:
- Use **backtracking**, placing one queen per row.
- Track used columns, positive diagonals, and negative diagonals:
  - col_set → columns under attack
  - pos_diag → (r + c) diagonal
  - neg_diag → (r - c) diagonal
- If a position (r, c) is safe:
  - Place queen → mark sets → recurse to next row → backtrack
- Build board from queen positions.

Time Complexity: O(n!)  
Space Complexity: O(n)
"""

class Solution(object):
    def solveNQueens(self, n):
        res = []
        board = [["."] * n for _ in range(n)]

        cols = set()
        pos_diag = set()   # r + c
        neg_diag = set()   # r - c

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                # Place queen
                board[r][c] = "Q"
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)

                backtrack(r + 1)

                # Remove queen (backtrack)
                board[r][c] = "."
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)

        backtrack(0)
        return res
