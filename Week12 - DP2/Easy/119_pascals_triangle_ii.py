"""
Problem: Pascal's Triangle II
LeetCode #119
Difficulty: Easy
Link: https://leetcode.com/problems/pascals-triangle-ii/

Problem Statement:
Given an integer rowIndex, return the rowIndex-th (0-indexed)
row of Pascal's Triangle.

In Pascal's Triangle:
- The first and last element of each row is 1.
- Each inner element is the sum of the two elements directly above it.

Examples:
Input: rowIndex = 3
Output: [1,3,3,1]

Input: rowIndex = 0
Output: [1]

Key Insight:
This is a **Dynamic Programming** problem optimized to use **O(k)** space.

We build the row in-place from right to left to avoid overwriting values
needed for computation.

Approach: Dynamic Programming (1D In-Place)
-------------------------------------------
Steps:
1. Initialize a list row with size rowIndex + 1 filled with 0s.
2. Set row[0] = 1.
3. For i from 1 to rowIndex:
   - Iterate j from i down to 1:
       row[j] = row[j] + row[j - 1]
4. Return row.

Time Complexity:
- O(rowIndex²)

Space Complexity:
- O(rowIndex)
"""

class Solution(object):
    def getRow(self, rowIndex):
        row = [0] * (rowIndex + 1)
        row[0] = 1

        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1):
                row[j] += row[j - 1]

        return row
