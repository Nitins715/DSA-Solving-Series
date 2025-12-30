"""
Problem: Minimum Falling Path Sum
LeetCode #931
Difficulty: Medium
Link: https://leetcode.com/problems/minimum-falling-path-sum/

Problem Statement:
Given an n x n array of integers matrix, return the minimum sum of any
falling path through matrix.

A falling path starts at any element in the first row and chooses
the element in the next row that is either directly below or
diagonally left/right.

Examples:
Input:
matrix = [
  [2,1,3],
  [6,5,4],
  [7,8,9]
]
Output: 13
Explanation:
The path 1 → 5 → 7 gives the minimum sum = 13

Input:
matrix = [
  [-19,57],
  [-40,-5]
]
Output: -59

Key Insight:
This is a **Dynamic Programming** problem.

To reach matrix[i][j], you can come from:
- matrix[i-1][j]   (up)
- matrix[i-1][j-1] (up-left)
- matrix[i-1][j+1] (up-right)

Approach: Dynamic Programming (In-Place)
----------------------------------------
Steps:
1. Start from the second row.
2. For each cell matrix[i][j]:
   - Add the minimum of the valid cells from the previous row.
3. The answer is the minimum value in the last row.

Time Complexity:
- O(n²)

Space Complexity:
- O(1) (in-place modification)
"""

class Solution(object):
    def minFallingPathSum(self, matrix):
        n = len(matrix)

        for i in range(1, n):
            for j in range(n):
                min_above = matrix[i - 1][j]
                if j > 0:
                    min_above = min(min_above, matrix[i - 1][j - 1])
                if j < n - 1:
                    min_above = min(min_above, matrix[i - 1][j + 1])

                matrix[i][j] += min_above

        return min(matrix[-1])
