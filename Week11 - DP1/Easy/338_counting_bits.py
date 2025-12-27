"""
Problem: Counting Bits
LeetCode #338
Difficulty: Easy
Link: https://leetcode.com/problems/counting-bits/

Problem Statement:
Given an integer n, return an array ans of length n + 1
where ans[i] is the number of 1's in the binary representation of i.

Examples:
Input: n = 2
Output: [0, 1, 1]
Explanation:
0 -> 0
1 -> 1
2 -> 10

Input: n = 5
Output: [0, 1, 1, 2, 1, 2]

Key Insight:
This is a **Dynamic Programming / Bit Manipulation** problem.

Observation:
- For any number i:
    number of set bits in i = number of set bits in (i >> 1) + (i & 1)

Approach: Dynamic Programming with Bit Manipulation
---------------------------------------------------
Steps:
1. Initialize an array dp of size n + 1 with all zeros.
2. For each number i from 1 to n:
   - dp[i] = dp[i >> 1] + (i & 1)
3. Return dp.

Time Complexity:
- O(n)

Space Complexity:
- O(n)
"""

class Solution(object):
    def countBits(self, n):
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)

        return dp
