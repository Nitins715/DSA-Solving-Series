"""
Problem: Spiral Matrix
LeetCode #54
Difficulty: Medium
Link: https://leetcode.com/problems/spiral-matrix/

Problem Statement:
Given an m x n matrix, return all elements of the matrix in spiral order.

Examples:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Approach:
- Use four pointers: top, bottom, left, right.
- Traverse boundaries and shrink them after each direction (right, down, left, up) until all elements visited.

Time Complexity: O(m*n)
Space Complexity: O(1) extra space (output not counted)
"""

class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        res = []
        top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1

        while top <= bottom and left <= right:
            # traverse right
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top += 1
            # traverse down
            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right -= 1
            if top <= bottom:
                # traverse left
                for i in range(right, left-1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
            if left <= right:
                # traverse up
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res
