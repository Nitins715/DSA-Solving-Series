"""
Problem: Subsets II
LeetCode #90
Difficulty: Medium
Link: https://leetcode.com/problems/subsets-ii/

Problem Statement:
Given an integer array nums that may contain duplicates,
return all possible subsets (the power set).

The solution set must not contain duplicate subsets.
Return the solution in any order.

Examples:
Input: nums = [1,2,2]
Output:
[
  [],
  [1],
  [1,2],
  [1,2,2],
  [2],
  [2,2]
]

Input: nums = [0]
Output: [[],[0]]

Approach:
- Sort the array so duplicate elements appear next to each other.
- Use **backtracking** to generate subsets.
- At each recursion level, if nums[i] == nums[i-1] and i > start,
  skip the element to avoid duplicate subsets.
- Always append a copy of the current path.

Time Complexity: O(2^n)
Space Complexity: O(2^n)
"""

class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        res = []

        def backtrack(start, path):
            res.append(list(path))

            for i in range(start, len(nums)):
                # Skip duplicates at the same level
                if i > start and nums[i] == nums[i - 1]:
                    continue

                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res
