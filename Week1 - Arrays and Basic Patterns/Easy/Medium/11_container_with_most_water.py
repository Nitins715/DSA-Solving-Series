"""
Problem: Container With Most Water
LeetCode #11
Difficulty: Medium
Link: https://leetcode.com/problems/container-with-most-water/

Problem Statement:
Given n non-negative integers `height` where each represents a point at coordinate (i, height[i]),
find two lines that together with x-axis form a container, such that the container contains the most water.

Examples:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

Approach:
- Use two pointers at both ends.
- Move the pointer with the smaller height inward.
- Track maximum area while moving pointers.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            max_area = max(max_area, h * w)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
