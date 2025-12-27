"""
Problem: Target Sum
LeetCode #494
Difficulty: Medium
Link: https://leetcode.com/problems/target-sum/

Problem Statement:
You are given an integer array nums and an integer target.
You want to build an expression by assigning either '+' or '-' in front of
each integer in nums and then concatenate all the integers.

Return the number of different expressions that evaluate to target.

Examples:
Input: nums = [1,1,1,1,1], target = 3
Output: 5

Input: nums = [1], target = 1
Output: 1

Key Insight:
This problem can be transformed into a **Subset Sum (Knapsack) DP** problem.

Let:
- Sum of all numbers = total_sum
- Suppose numbers with '+' sum to P
- Numbers with '-' sum to N

We know:
P - N = target
P + N = total_sum

Solving:
P = (target + total_sum) / 2

So the problem becomes:
👉 Count the number of subsets with sum = P

If (target + total_sum) is odd or |target| > total_sum → return 0.

Approach: Dynamic Programming (Subset Sum Count)
------------------------------------------------
Let dp[s] = number of ways to achieve sum s.

Steps:
1. Compute total_sum of nums.
2. Check feasibility:
   - If total_sum < |target| or (target + total_sum) is odd → return 0
3. Compute required subset sum P.
4. Initialize dp array of size P + 1:
   - dp[0] = 1
5. For each number in nums:
   - Iterate s from P down to num:
       dp[s] += dp[s - num]
6. Return dp[P]

Time Complexity:
- O(n × P), where P = (target + total_sum) / 2

Space Complexity:
- O(P)
"""

class Solution(object):
    def findTargetSumWays(self, nums, target):
        total_sum = sum(nums)

        # Feasibility check
        if total_sum < abs(target) or (total_sum + target) % 2 != 0:
            return 0

        P = (total_sum + target) // 2

        dp = [0] * (P + 1)
        dp[0] = 1

        for num in nums:
            for s in range(P, num - 1, -1):
                dp[s] += dp[s - num]

        return dp[P]
