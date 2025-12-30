"""
Problem: Largest Divisible Subset
LeetCode #368
Difficulty: Medium
Link: https://leetcode.com/problems/largest-divisible-subset/

Problem Statement:
Given a set of distinct positive integers nums, return the largest subset
such that for every pair (a, b) in the subset:
- a % b == 0 or
- b % a == 0

If there are multiple solutions, return any of them.

Examples:
Input: nums = [1,2,3]
Output: [1,2] (or [1,3])

Input: nums = [1,2,4,8]
Output: [1,2,4,8]

Key Insight:
This is similar to **Longest Increasing Subsequence (LIS)**,
but instead of increasing order, we check **divisibility**.

By sorting the array, if nums[i] % nums[j] == 0 (j < i),
then nums[j] can precede nums[i] in the subset.

Approach: Dynamic Programming + Backtracking
--------------------------------------------
Let:
- dp[i] = length of largest divisible subset ending at index i
- parent[i] = previous index in the subset chain

Steps:
1. Sort nums in ascending order.
2. Initialize:
   - dp[i] = 1 (each number alone)
   - parent[i] = -1
3. For each i from 0 to n-1:
   - For each j from 0 to i-1:
       If nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
           dp[i] = dp[j] + 1
           parent[i] = j
4. Find index with maximum dp value.
5. Reconstruct the subset using parent pointers.
6. Return the subset.

Time Complexity:
- O(n²)

Space Complexity:
- O(n)
"""

class Solution(object):
    def largestDivisibleSubset(self, nums):
        if not nums:
            return []

        nums.sort()
        n = len(nums)

        dp = [1] * n
        parent = [-1] * n

        max_len = 1
        max_idx = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        parent[i] = j

            if dp[i] > max_len:
                max_len = dp[i]
                max_idx = i

        # Reconstruct subset
        result = []
        while max_idx != -1:
            result.append(nums[max_idx])
            max_idx = parent[max_idx]

        return result[::-1]
