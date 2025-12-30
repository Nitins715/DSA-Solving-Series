"""
Problem: Climbing Stairs
LeetCode #70
Difficulty: Easy
Link: https://leetcode.com/problems/climbing-stairs/

Problem Statement:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps.

In how many distinct ways can you climb to the top?

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

Key Insight:
This is a classic **Dynamic Programming** problem.
The number of ways to reach step n depends on:
- ways to reach step n-1
- ways to reach step n-2

This forms a Fibonacci-like recurrence.

Approach: Dynamic Programming (Space Optimized)
-----------------------------------------------
Let:
- prev2 = ways to reach step n-2
- prev1 = ways to reach step n-1

Steps:
1. Handle base cases:
   - If n <= 2 → return n
2. Initialize prev2 = 1, prev1 = 2
3. Iterate from step 3 to n:
   - current = prev1 + prev2
   - Slide the window
4. Return prev1

Time Complexity:
- O(n)

Space Complexity:
- O(1)
"""

class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n

        prev2 = 1  # ways to reach step 1
        prev1 = 2  # ways to reach step 2

        for _ in range(3, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr

        return prev1
