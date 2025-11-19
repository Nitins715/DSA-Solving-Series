"""
Problem: Pascal's Triangle II
LeetCode #119
Difficulty: Easy
Link: https://leetcode.com/problems/pascals-triangle-ii/

Problem Statement:
Given an integer rowIndex, return the rowIndexth (0-indexed) row of Pascal's Triangle.

In Pascal's triangle:
- Each number is the sum of the two numbers directly above it.

Examples:
Input: rowIndex = 3
Output: [1,3,3,1]

Input: rowIndex = 0
Output: [1]

Input: rowIndex = 1
Output: [1,1]

Approach:
- We only need one row at a time, so we can use a 1D list.
- For each iteration, update the list from right to left to avoid overwriting values.
- Start from [1] and update it row by row.

Time Complexity: O(n²)
Space Complexity: O(n)
"""

class Solution(object):
    def getRow(self, rowIndex):
        row = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                row[j] += row[j - 1]
        return row
