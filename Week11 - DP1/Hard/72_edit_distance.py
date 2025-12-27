"""
Problem: Edit Distance
LeetCode #72
Difficulty: Medium
Link: https://leetcode.com/problems/edit-distance/

Problem Statement:
Given two strings word1 and word2, return the minimum number of operations
required to convert word1 into word2.

You are allowed the following operations on a word:
1. Insert a character
2. Delete a character
3. Replace a character

Examples:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Input: word1 = "intention", word2 = "execution"
Output: 5

Key Insight:
This is a classic **Dynamic Programming** problem.

Let dp[i][j] be the minimum number of operations required to convert
the first i characters of word1 into the first j characters of word2.

Approach: Dynamic Programming (2D DP)
-------------------------------------
Steps:
1. Create a DP table of size (m+1) x (n+1),
   where m = len(word1), n = len(word2).
2. Base cases:
   - dp[i][0] = i (delete all characters)
   - dp[0][j] = j (insert all characters)
3. Fill the table:
   - If word1[i-1] == word2[j-1]:
       dp[i][j] = dp[i-1][j-1]
   - Else:
       dp[i][j] = 1 + min(
           dp[i-1][j],    # delete
           dp[i][j-1],    # insert
           dp[i-1][j-1]   # replace
       )
4. Return dp[m][n].

Time Complexity:
- O(m × n)

Space Complexity:
- O(m × n)
"""

class Solution(object):
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)

        # DP table initialization
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base cases
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        # Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],    # delete
                        dp[i][j - 1],    # insert
                        dp[i - 1][j - 1] # replace
                    )

        return dp[m][n]
