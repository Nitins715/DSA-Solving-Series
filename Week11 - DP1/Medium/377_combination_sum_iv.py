"""
Problem: Combination Sum IV
LeetCode #377
Difficulty: Medium
Link: https://leetcode.com/problems/combination-sum-iv/

Problem Statement:
You are given an array of distinct integers nums and a target integer target.
Return the number of possible combinations that add up to target.

Note:
- Different sequences are counted as different combinations.
- You may assume all numbers in nums are positive.

Examples:
Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combinations are:
(1,1,1,1)
(1,1,2)
(1,2,1)
(2,1,1)
(2,2)
(1,3)
(3,1)

Input: nums = [9], target = 3
Output: 0

Key Insight:
This is a **Dynamic Programming** problem.
Order matters, so we build solutions based on increasing target values.

Approach: Dynamic Programming (Permutation-based)
-------------------------------------------------
Let dp[i] = number of combinations that sum to i.

Steps:
1. Initialize dp array of size target + 1:
   - dp[0] = 1 (one way to make sum 0: choose nothing)
2. For each sum i from 1 to target:
   - For each number num in nums:
       - If num <= i:
           dp[i] += dp[i - num]
3. Return dp[target]

Time Complexity:
- O(target × len(nums))

Space Complexity:
- O(target)
"""

class Solution(object):
    def combinationSum4(self, nums, target):
        dp = [0] * (target + 1)
        dp[0] = 1

        for curr_sum in range(1, target + 1):
            for num in nums:
                if num <= curr_sum:
                    dp[curr_sum] += dp[curr_sum - num]

        return dp[target]
