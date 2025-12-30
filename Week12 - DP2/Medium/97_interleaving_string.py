# File Name: 97_interleaving_string.py

"""
Problem: Interleaving String
LeetCode #97
Difficulty: Medium
Link: https://leetcode.com/problems/interleaving-string/

Problem Statement:
Given strings s1, s2, and s3, determine whether s3 is formed by an interleaving
of s1 and s2.

An interleaving of two strings s and t is a configuration where:
- s and t are divided into substrings
- These substrings are interleaved together
- The relative order of characters in s and t is preserved

Examples:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: True

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: False

Input: s1 = "", s2 = "", s3 = ""
Output: True

Key Insight:
This is a **Dynamic Programming** problem.

Let dp[i][j] = True if s3[0 : i + j] can be formed by interleaving
s1[0 : i] and s2[0 : j].

Approach: Dynamic Programming (2D DP)
-------------------------------------
Steps:
1. If len(s1) + len(s2) != len(s3), return False immediately.
2. Create a DP table of size (len(s1) + 1) x (len(s2) + 1).
3. Base case:
   - dp[0][0] = True
4. Fill the table:
   - dp[i][j] is True if:
       a) dp[i-1][j] is True and s1[i-1] == s3[i+j-1]
       OR
       b) dp[i][j-1] is True and s2[j-1] == s3[i+j-1]
5. Return dp[len(s1)][len(s2)].

Time Complexity:
- O(len(s1) × len(s2))

Space Complexity:
- O(len(s1) × len(s2))
"""

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        m, n = len(s1), len(s2)

        # Length mismatch check
        if m + n != len(s3):
            return False

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # Fill first row
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        # Fill first column
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        # Fill rest of DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = (
                    (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or
                    (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
                )

        return dp[m][n]
