"""
Problem: Word Break
LeetCode #139
Difficulty: Medium
Link: https://leetcode.com/problems/word-break/

Problem Statement:
Given a string s and a dictionary of strings wordDict,
return True if s can be segmented into a space-separated
sequence of one or more dictionary words.

Each word in the dictionary can be used multiple times.

Examples:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: True

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: True

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: False

Key Insight:
This is a **Dynamic Programming** problem.
We check whether prefixes of the string can be formed
using the dictionary words.

Approach: Dynamic Programming
-----------------------------
Let dp[i] = True if substring s[0:i] can be segmented.

Steps:
1. Convert wordDict to a set for O(1) lookups.
2. Initialize dp array of size len(s) + 1:
   - dp[0] = True (empty string)
3. For i from 1 to len(s):
   - For j from 0 to i-1:
       - If dp[j] is True and s[j:i] in wordDict:
           dp[i] = True
           break
4. Return dp[len(s)]

Time Complexity:
- O(n²) where n = length of string

Space Complexity:
- O(n)
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        word_set = set(wordDict)
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]
