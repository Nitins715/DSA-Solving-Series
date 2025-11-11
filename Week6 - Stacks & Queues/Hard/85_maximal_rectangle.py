"""
Problem: Maximal Rectangle
LeetCode #85
Difficulty: Hard
Link: https://leetcode.com/problems/maximal-rectangle/

Problem Statement:
Given a rows x cols binary matrix filled with 0's and 1's, 
find the largest rectangle containing only 1's and return its area.

Examples:
Input: matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6

Explanation:
The maximal rectangle of 1's is formed in the middle with area = 6.

Approach:
- Treat each row of the matrix as the base of a histogram.
- For every row, compute the "height" of consecutive 1's for each column.
- Use the **Largest Rectangle in Histogram** technique (LeetCode #84) for each row:
  - Maintain a stack of indices.
  - For each column, pop while the current bar is smaller than the top of the stack
    to compute areas.
- Keep track of the maximum rectangle area across all rows.

Time Complexity: O(m * n)
Space Complexity: O(n)
"""

class Solution(object):
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        n = len(matrix[0])
        heights = [0] * n
        max_area = 0

        for row in matrix:
            # Build the histogram height for current row
            for i in range(n):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0

            # Compute the largest rectangle in current histogram
            max_area = max(max_area, self.largestRectangleArea(heights))

        return max_area

    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        heights.append(0)  # Sentinel to flush out remaining bars

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        heights.pop()  # Remove sentinel
        return max_area
