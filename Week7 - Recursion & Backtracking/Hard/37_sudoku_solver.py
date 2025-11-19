"""
Problem: Sudoku Solver
LeetCode #37
Difficulty: Hard
Link: https://leetcode.com/problems/sudoku-solver/

Problem Statement:
Write a program to solve a 9x9 Sudoku puzzle by filling the empty cells.

Rules:
- Digits 1-9 must appear exactly once in each row.
- Digits 1-9 must appear exactly once in each column.
- Digits 1-9 must appear exactly once in each 3x3 sub-box.
- The board contains characters '1'-'9' and '.' for empty cells.
- There is always exactly one valid solution.

Approach:
- Use **backtracking**.
- Traverse each cell to find an empty spot '.'.
- Try placing digits '1' to '9':
    - If valid (row, column, box constraints), place and recurse.
    - If recursion fails → undo and try next digit.
- Once the board is filled without conflicts → solved.

Validation:
- Row check: used numbers cannot repeat.
- Column check: used numbers cannot repeat.
- Box check: used numbers cannot repeat.

Time Complexity: O(9^(n)) worst case  
Space Complexity: O(1)  (in-place)
"""

class Solution(object):
    def solveSudoku(self, board):
        def is_valid(r, c, ch):
            # Check row
            for i in range(9):
                if board[r][i] == ch:
                    return False

            # Check column
            for i in range(9):
                if board[i][c] == ch:
                    return False

            # Check 3x3 sub-box
            box_r = (r // 3) * 3
            box_c = (c // 3) * 3
            for i in range(box_r, box_r + 3):
                for j in range(box_c, box_c + 3):
                    if board[i][j] == ch:
                        return False

            return True

        def backtrack():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for ch in '123456789':
                            if is_valid(r, c, ch):
                                board[r][c] = ch
                                if backtrack():
                                    return True
                                board[r][c] = '.'  # Undo
                        return False  # No valid digit → backtrack
            return True  # Filled all cells

        backtrack()
