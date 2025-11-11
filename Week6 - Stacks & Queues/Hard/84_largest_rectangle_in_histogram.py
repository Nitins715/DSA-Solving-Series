"""
Problem: Largest Rectangle in Histogram
LeetCode #84
Difficulty: Hard
Link: https://leetcode.com/problems/largest-rectangle-in-histogram/

Problem Statement:
Given an array of integers heights representing the histogram's bar height 
where the width of each bar is 1, return the area of the largest rectangle 
in the histogram.

Examples:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The largest rectangle has an area = 5 * 2 = 10 (bars with height 5 and 6).

Input: heights = [2,4]
Output: 4

Approach:
- Use a **monotonic increasing stack** to efficiently calculate the largest rectangle.
- Traverse each bar:
  - While the current height is smaller than the height at the top of the stack:
    - Pop from stack and compute the area of the rectangle formed with that bar as height.
  - Push the current index to the stack.
- Append a sentinel value `0` at the end to ensure all bars are processed.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []  # Stack to store indices of bars
        max_area = 0
        heights.append(0)  # Sentinel to flush out remaining bars

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                # Width is current index if stack is empty, else distance from previous bar
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        heights.pop()  # Remove sentinel
        return max_area
