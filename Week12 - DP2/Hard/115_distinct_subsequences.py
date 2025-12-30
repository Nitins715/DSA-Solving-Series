"""
Problem: Distinct Subsequences
LeetCode #115
Difficulty: Hard
Link: https://leetcode.com/problems/distinct-subsequences/

Problem Statement:
Given two strings s and t, return the number of distinct subsequences of s
which equals t.

A subsequence of a string is a new string formed from the original string
by deleting some (can be none) of the characters without disturbing the
relative positions of the remaining characters.

Examples:
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
There are 3 ways to delete one 'b' from s to form "rabbit".

Input: s = "babgbag", t = "bag"
Output: 5

Key Insight:
This is a **Dynamic Programming** problem.

Let dp[i][j] be the number of distinct subsequences of
s[0:i] that equal t[0:j].

Approach: Dynamic Programming (2D DP)
-------------------------------------
Steps:
1. Let m = len(s), n = len(t).
2. Create a DP table of size (m+1) x (n+1).
3. Base cases:
   - dp[i][0] = 1 for all i (empty t can be formed in 1 way)
   - dp[0][j] = 0 for j > 0 (non-empty t cannot be formed from empty s)
4. Transition:
   - If s[i-1] == t[j-1]:
       dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
   - Else:
       dp[i][j] = dp[i-1][j]
5. Return dp[m][n].

Time Complexity:
- O(m × n)

Space Complexity:
- O(m × n)
"""

class Solution(object):
    def numDistinct(self, s, t):
        m, n = len(s), len(t)

        # dp[i][j] = number of ways s[0:i] forms t[0:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base case: empty t
        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[m][n]
