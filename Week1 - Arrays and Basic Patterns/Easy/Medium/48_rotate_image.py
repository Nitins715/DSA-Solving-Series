"""
Problem: Rotate Image
LeetCode #48
Difficulty: Medium
Link: https://leetcode.com/problems/rotate-image/

Problem Statement:
You are given an n x n 2D matrix representing an image. Rotate the image by 90 degrees (clockwise) in-place.

Examples:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Approach:
- Transpose the matrix.
- Reverse each row to get the rotated matrix.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        # Transpose
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reverse each row
        for row in matrix:
            row.reverse()
