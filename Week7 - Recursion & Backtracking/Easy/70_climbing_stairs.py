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
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Approach:
- This is a classic Dynamic Programming (DP) problem similar to the Fibonacci sequence.
- The number of ways to reach step `n` = ways(n-1) + ways(n-2):
  - ways(n-1): reaching from one step below
  - ways(n-2): reaching from two steps below
- Base cases:
  - n = 1 → 1 way
  - n = 2 → 2 ways
- Can be optimized to O(1) space using two variables.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n

        one, two = 1, 2  # ways to reach step 1 and step 2
        for _ in range(3, n + 1):
            one, two = two, one + two  # slide window

        return two
