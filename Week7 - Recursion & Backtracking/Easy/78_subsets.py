"""
Problem: Subsets
LeetCode #78
Difficulty: Medium
Link: https://leetcode.com/problems/subsets/

Problem Statement:
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Examples:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Input: nums = [0]
Output: [[],[0]]

Approach:
- Use **backtracking** to explore all inclusion/exclusion possibilities.
- At each index, decide:
  - Include current element.
  - Exclude current element.
- Append a copy of the current subset at each recursive call.

Alternative:
- Can also be done iteratively by extending existing subsets with each new element.

Time Complexity: O(2^n)
Space Complexity: O(2^n)
"""

class Solution(object):
    def subsets(self, nums):
        res = []

        def backtrack(start, path):
            # Append a copy of the current subset
            res.append(list(path))

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res
