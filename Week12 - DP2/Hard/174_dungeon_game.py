"""
Problem: Dungeon Game
LeetCode #174
Difficulty: Hard
Link: https://leetcode.com/problems/dungeon-game/

Problem Statement:
The demons had captured the princess and imprisoned her in the bottom-right
corner of a dungeon. The dungeon consists of m x n rooms laid out in a grid.

Our brave knight starts in the top-left room and needs to reach the princess.
The knight can only move right or down.

Each room contains:
- a positive integer (health increase)
- a negative integer (health decrease)
- zero (no effect)

The knight's health must never drop to 0 or below.

Return the knight's minimum initial health so that he can rescue the princess.

Examples:
Input:
dungeon = [
  [-2, -3,  3],
  [-5, -10, 1],
  [10, 30, -5]
]
Output: 7

Key Insight:
This is a **Dynamic Programming** problem solved in reverse.

Instead of tracking max health gained, we track the **minimum health needed**
to enter each cell so that the knight can safely reach the destination.

Approach: Dynamic Programming (Bottom-Up from Destination)
----------------------------------------------------------
Let dp[i][j] = minimum health needed to enter cell (i, j).

Steps:
1. Create a DP table of size (m+1) x (n+1) initialized with infinity.
2. Set:
   - dp[m][n-1] = 1
   - dp[m-1][n] = 1
   (These act as sentinels for the princess cell.)
3. Traverse the grid from bottom-right to top-left:
   - dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
4. Return dp[0][0].

Time Complexity:
- O(m × n)

Space Complexity:
- O(m × n)
"""

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])

        INF = float('inf')
        dp = [[INF] * (n + 1) for _ in range(m + 1)]

        # Sentinel values
        dp[m][n - 1] = 1
        dp[m - 1][n] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                need = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                dp[i][j] = max(1, need)

        return dp[0][0]
