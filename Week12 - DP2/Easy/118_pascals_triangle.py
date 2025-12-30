"""
Problem: Pascal's Triangle
LeetCode #118
Difficulty: Easy
Link: https://leetcode.com/problems/pascals-triangle/

Problem Statement:
Given an integer numRows, return the first numRows of Pascal's Triangle.

In Pascal's Triangle:
- The first and last element of each row is 1.
- Every other element is the sum of the two elements directly above it.

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

Key Insight:
This is a **Dynamic Programming / Simulation** problem.
Each row is built using the previous row.

Approach: Dynamic Programming
-----------------------------
Steps:
1. Initialize an empty list result.
2. For each row i from 0 to numRows - 1:
   - Start row with all 1s.
   - For positions j from 1 to i-1:
       row[j] = previous_row[j-1] + previous_row[j]
   - Append row to result.
3. Return result.

Time Complexity:
- O(numRows²)

Space Complexity:
- O(numRows²)
"""

class Solution(object):
    def generate(self, numRows):
        result = []

        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = result[i - 1][j - 1] + result[i - 1][j]
            result.append(row)

        return result
