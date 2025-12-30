"""
Problem: Triangle
LeetCode #120
Difficulty: Medium
Link: https://leetcode.com/problems/triangle/

Problem Statement:
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below.
More formally, if you are on index j on the current row, you may move to:
- index j
- index j + 1
on the next row.

Examples:
Input: triangle = [[2],
                   [3,4],
                   [6,5,7],
                   [4,1,8,3]]
Output: 11
Explanation:
The path 2 → 3 → 5 → 1 has the minimum sum = 11

Input: triangle = [[-10]]
Output: -10

Key Insight:
This is a **Dynamic Programming** problem.

Each cell depends only on the two cells directly below it.
We can solve this efficiently using **bottom-up DP** and modify the triangle in place.

Approach: Dynamic Programming (Bottom-Up, In-Place)
---------------------------------------------------
Steps:
1. Start from the second last row and move upwards.
2. For each element triangle[i][j]:
   - triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
3. After processing the top row, triangle[0][0] contains the answer.

Time Complexity:
- O(n²), where n is the number of rows

Space Complexity:
- O(1) (in-place modification)
"""

class Solution(object):
    def minimumTotal(self, triangle):
        # Start from the second last row
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(
                    triangle[i + 1][j],
                    triangle[i + 1][j + 1]
                )

        return triangle[0][0]
