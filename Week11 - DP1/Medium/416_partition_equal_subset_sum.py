"""
Problem: Partition Equal Subset Sum
LeetCode #416
Difficulty: Medium
Link: https://leetcode.com/problems/partition-equal-subset-sum/

Problem Statement:
Given a non-empty array nums containing only positive integers,
determine if the array can be partitioned into two subsets such that
the sum of elements in both subsets is equal.

Examples:
Input: nums = [1,5,11,5]
Output: True
Explanation:
The array can be partitioned as [1,5,5] and [11]

Input: nums = [1,2,3,5]
Output: False

Key Insight:
This is a **0/1 Knapsack (Subset Sum)** problem.

If total_sum is odd, it is impossible to split into two equal subsets.
Otherwise, the problem reduces to checking if there exists a subset
with sum = total_sum / 2.

Approach: Dynamic Programming (Subset Sum)
------------------------------------------
Let target = total_sum / 2.

Let dp[s] = True if a subset with sum s is achievable.

Steps:
1. Compute total_sum.
2. If total_sum is odd → return False.
3. Initialize dp array of size target + 1:
   - dp[0] = True
4. For each num in nums:
   - Iterate s from target down to num:
       dp[s] = dp[s] or dp[s - num]
5. Return dp[target].

Time Complexity:
- O(n × target)

Space Complexity:
- O(target)
"""

class Solution(object):
    def canPartition(self, nums):
        total_sum = sum(nums)

        # If total sum is odd, cannot partition equally
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for s in range(target, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]

        return dp[target]
