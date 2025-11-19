"""
Problem: Pascal's Triangle
LeetCode #118
Difficulty: Easy
Link: https://leetcode.com/problems/pascals-triangle/

Problem Statement:
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle:
- Each number is the sum of the two numbers directly above it.

Examples:
Input: numRows = 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

Input: numRows = 1
Output: [[1]]

Approach:
- Initialize the triangle with the first row [1].
- For each new row i:
  - Start and end with 1.
  - Each middle element = sum of two elements from the previous row.
- Append each generated row to the triangle.

Time Complexity: O(n²)
Space Complexity: O(n²)
"""

class Solution(object):
    def generate(self, numRows):
        triangle = []

        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)

        return triangle
