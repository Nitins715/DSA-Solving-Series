# File Name: 300_longest_increasing_subsequence.py

"""
Problem: Longest Increasing Subsequence
LeetCode #300
Difficulty: Medium
Link: https://leetcode.com/problems/longest-increasing-subsequence/

Problem Statement:
Given an integer array nums, return the length of the longest
strictly increasing subsequence.

A subsequence is a sequence that can be derived from the array
by deleting some or no elements without changing the order
of the remaining elements.

Examples:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation:
The longest increasing subsequence is [2,3,7,101]

Input: nums = [0,1,0,3,2,3]
Output: 4

Key Insight:
This is a **Dynamic Programming** problem.
For each index i, compute the length of the LIS ending at i.

Approach 1: Dynamic Programming (O(n²))
---------------------------------------
Let dp[i] = length of LIS ending at index i.

Steps:
1. Initialize dp array of size n with all values = 1
2. For each i from 0 to n-1:
   - For each j from 0 to i-1:
       - If nums[j] < nums[i]:
           dp[i] = max(dp[i], dp[j] + 1)
3. Return max(dp)

Time Complexity:
- O(n²)

Space Complexity:
- O(n)
"""

class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
