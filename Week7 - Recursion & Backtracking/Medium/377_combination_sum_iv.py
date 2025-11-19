"""
Problem: Combination Sum IV
LeetCode #377
Difficulty: Medium
Link: https://leetcode.com/problems/combination-sum-iv/

Problem Statement:
Given an array of distinct integers nums and a target integer target,
return the number of possible combinations that add up to target.

The order of the numbers matters.

Examples:
Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
Possible combinations:
(1,1,1,1)
(1,1,2)
(1,2,1)
(2,1,1)
(1,3)
(3,1)
(2,2)

Input: nums = [9], target = 3
Output: 0

Approach:
- Use **Dynamic Programming (DP)** because we want the number of ordered combinations.
- Let dp[i] represent the number of ways to make sum i.
- Initialization:
  dp[0] = 1  (one way to reach 0 → choose nothing)
- For each total from 1 to target:
  - For each num in nums:
      If num <= total, add dp[total - num] to dp[total].
- Return dp[target].

This is like counting permutations, not combinations.

Time Complexity: O(n * target)
Space Complexity: O(target)
"""

class Solution(object):
    def combinationSum4(self, nums, target):
        dp = [0] * (target + 1)
        dp[0] = 1  # Base case

        for total in range(1, target + 1):
            for num in nums:
                if num <= total:
                    dp[total] += dp[total - num]

        return dp[target]
