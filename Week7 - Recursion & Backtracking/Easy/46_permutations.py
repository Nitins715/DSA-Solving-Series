"""
Problem: Permutations
LeetCode #46
Difficulty: Medium
Link: https://leetcode.com/problems/permutations/

Problem Statement:
Given an array nums of distinct integers, return all possible permutations.
You can return the answer in any order.

Examples:
Input: nums = [1,2,3]
Output: 
[[1,2,3],
 [1,3,2],
 [2,1,3],
 [2,3,1],
 [3,1,2],
 [3,2,1]]

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Input: nums = [1]
Output: [[1]]

Approach:
- Use **backtracking** to generate all permutations.
- At each recursive call:
  - Choose one unused element.
  - Add it to the current path.
  - Recurse with the remaining elements.
  - Backtrack by removing the last chosen element.

Alternative:
- Use itertools.permutations for a one-liner, but backtracking gives better insight into recursion.

Time Complexity: O(n!)
Space Complexity: O(n!)
"""

class Solution(object):
    def permute(self, nums):
        res = []
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(list(path))
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False

        backtrack([])
        return res
