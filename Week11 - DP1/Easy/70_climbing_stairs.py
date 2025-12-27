"""
Problem: Climbing Stairs
LeetCode #70
Difficulty: Easy
Link: https://leetcode.com/problems/climbing-stairs/

Problem Statement:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps.

In how many distinct ways can you climb to the top?

This problem is a classic **Dynamic Programming** problem
and is equivalent to computing the **Fibonacci sequence**.

Examples:
Input: n = 2
Output: 2
Explanation:
1. 1 step + 1 step
2. 2 steps

Input: n = 3
Output: 3
Explanation:
1. 1 + 1 + 1
2. 1 + 2
3. 2 + 1

Approach: Dynamic Programming (Optimized Fibonacci)
---------------------------------------------------
Key idea:
- To reach step n, you must come from:
  - step (n-1) using 1 step
  - step (n-2) using 2 steps
- So:
    dp[n] = dp[n-1] + dp[n-2]

Steps:
1. Handle base cases:
   - If n == 1 → return 1
   - If n == 2 → return 2
2. Use two variables to store previous two results.
3. Iterate from 3 to n and update values.
4. Return the result for n.

Time Complexity:
- O(n)

Space Complexity:
- O(1) (constant space)
"""

class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2

        prev2 = 1  # ways to reach step 1
        prev1 = 2  # ways to reach step 2

        for _ in range(3, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr

        return prev1
