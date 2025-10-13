"""
Problem: Merge Intervals
LeetCode #56
Difficulty: Medium
Link: https://leetcode.com/problems/merge-intervals/

Problem Statement:
Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Examples:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

Approach:
- Sort intervals by start time.
- Iterate through intervals and merge overlapping ones.
- Append merged intervals to the result.

Time Complexity: O(n log n) due to sorting
Space Complexity: O(n)
"""

class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for current in intervals[1:]:
            last = merged[-1]
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)

        return merged
    