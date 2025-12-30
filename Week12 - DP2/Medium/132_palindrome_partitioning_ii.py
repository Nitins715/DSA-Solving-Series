"""
Problem: Palindrome Partitioning II
LeetCode #132
Difficulty: Hard
Link: https://leetcode.com/problems/palindrome-partitioning-ii/

Problem Statement:
Given a string s, partition s such that every substring of the partition
is a palindrome.

Return the minimum number of cuts needed for a palindrome partitioning of s.

Examples:
Input: s = "aab"
Output: 1
Explanation:
The palindrome partitioning ["aa","b"] could be produced using 1 cut.

Input: s = "a"
Output: 0

Input: s = "ab"
Output: 1

Key Insight:
This problem combines **Palindrome Checking + Dynamic Programming**.

We need:
1. Fast palindrome lookup for any substring.
2. DP to compute the minimum cuts needed.

Approach: Dynamic Programming with Palindrome Preprocessing
-----------------------------------------------------------
Let:
- isPal[i][j] = True if s[i:j+1] is a palindrome
- dp[i] = minimum cuts needed for substring s[0:i+1]

Steps:
1. Precompute isPal using DP:
   - A substring is palindrome if:
     s[i] == s[j] and (j - i <= 2 or isPal[i+1][j-1])
2. Initialize dp array:
   - dp[i] = i (worst case: cut before every character)
3. For each end index i:
   - If s[0:i+1] is palindrome → dp[i] = 0
   - Else:
       dp[i] = min(dp[j-1] + 1) for all j ≤ i where s[j:i+1] is palindrome
4. Return dp[n-1]

Time Complexity:
- O(n²)

Space Complexity:
- O(n²)
"""

class Solution(object):
    def minCut(self, s):
        n = len(s)
        if n <= 1:
            return 0

        # Palindrome lookup table
        isPal = [[False] * n for _ in range(n)]

        for end in range(n):
            for start in range(end + 1):
                if s[start] == s[end] and (end - start <= 2 or isPal[start + 1][end - 1]):
                    isPal[start][end] = True

        # dp[i] = min cuts for s[0:i+1]
        dp = [0] * n
        for i in range(n):
            dp[i] = i  # max cuts

            if isPal[0][i]:
                dp[i] = 0
            else:
                for j in range(1, i + 1):
                    if isPal[j][i]:
                        dp[i] = min(dp[i], dp[j - 1] + 1)

        return dp[-1]
