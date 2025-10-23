"""
Problem: Valid Sudoku  
LeetCode #36  
Difficulty: Medium  
Link: https://leetcode.com/problems/valid-sudoku/  

Problem Statement:  
Determine if a 9 x 9 Sudoku board is valid.  
Only the filled cells need to be validated according to the following rules:  
1. Each row must contain the digits 1–9 without repetition.  
2. Each column must contain the digits 1–9 without repetition.  
3. Each of the nine 3x3 sub-boxes must contain the digits 1–9 without repetition.  

Note:  
- A Sudoku board (partially filled) could be valid but not necessarily solvable.  
- Only the filled cells (non '.') need to be checked.

Examples:  
Input:  
board =  
[["5","3",".",".","7",".",".",".","."],  
 ["6",".",".","1","9","5",".",".","."],  
 [".","9","8",".",".",".",".","6","."],  
 ["8",".",".",".","6",".",".",".","3"],  
 ["4",".",".","8",".","3",".",".","1"],  
 ["7",".",".",".","2",".",".",".","6"],  
 [".","6",".",".",".",".","2","8","."],  
 [".",".",".","4","1","9",".",".","5"],  
 [".",".",".",".","8",".",".","7","9"]]  

Output: true  

Approach:  
- Use sets to track seen numbers for each row, column, and 3x3 sub-box.  
- For every filled cell (not '.'), check:
  - If number already exists in its row → invalid  
  - If number already exists in its column → invalid  
  - If number already exists in its sub-box → invalid  
- Otherwise, record it in all three sets and continue.  
- If no rule is violated, the board is valid.

Time Complexity: O(1) — fixed 9x9 board  
Space Complexity: O(1) — fixed sets for 9 rows, columns, and boxes
"""

class Solution:
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue

                box_index = (i // 3) * 3 + (j // 3)

                if num in rows[i] or num in cols[j] or num in boxes[box_index]:
                    return False

                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)

        return True
