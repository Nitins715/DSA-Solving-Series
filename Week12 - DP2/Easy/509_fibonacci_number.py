"""
Problem: Fibonacci Number
LeetCode #509
Difficulty: Easy
Link: https://leetcode.com/problems/fibonacci-number/

Problem Statement:
The Fibonacci numbers, commonly denoted F(n), form a sequence such that:
- F(0) = 0
- F(1) = 1
- F(n) = F(n - 1) + F(n - 2) for n > 1

Given an integer n, return F(n).

Examples:
Input: n = 2
Output: 1

Input: n = 3
Output: 2

Input: n = 4
Output: 3

Key Insight:
This is a classic **Dynamic Programming** problem.
Each Fibonacci number depends on the previous two numbers.

Approach: Iterative Dynamic Programming (Space Optimized)
---------------------------------------------------------
Steps:
1. Handle base cases n = 0 and n = 1.
2. Use two variables to track the previous two Fibonacci numbers.
3. Iterate from 2 to n and update values.
4. Return the result.

Time Complexity:
- O(n)

Space Complexity:
- O(1)
"""

class Solution(object):
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1

        prev2 = 0  # F(0)
        prev1 = 1  # F(1)

        for _ in range(2, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr

        return prev1
