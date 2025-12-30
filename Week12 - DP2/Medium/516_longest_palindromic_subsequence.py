# File Name: 516_longest_palindromic_subsequence.py

"""
Problem: Longest Palindromic Subsequence
LeetCode #516
Difficulty: Medium
Link: https://leetcode.com/problems/longest-palindromic-subsequence/

Problem Statement:
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence
by deleting some or no elements without changing the order of the
remaining elements.

Examples:
Input: s = "bbbab"
Output: 4
Explanation:
The longest palindromic subsequence is "bbbb"

Input: s = "cbbd"
Output: 2
Explanation:
The longest palindromic subsequence is "bb"

Key Insight:
This is a **Dynamic Programming** problem.

Let dp[i][j] be the length of the longest palindromic subsequence
in substring s[i : j + 1].

Approach: Dynamic Programming (2D DP)
-------------------------------------
Steps:
1. Create a DP table dp of size n x n.
2. Base case:
   - dp[i][i] = 1 (single character)
3. Fill the table for increasing substring lengths:
   - If s[i] == s[j]:
       dp[i][j] = 2 + dp[i + 1][j - 1]
   - Else:
       dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
4. Return dp[0][n - 1].

Time Complexity:
- O(n²)

Space Complexity:
- O(n²)
"""

class Solution(object):
    def longestPalindromeSubseq(self, s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        # Single characters are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1

        # Build for substrings of increasing length
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    dp[i][j] = 2 + (dp[i + 1][j - 1] if length > 2 else 0)
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]
