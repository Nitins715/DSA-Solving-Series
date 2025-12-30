"""
Problem: Coin Change
LeetCode #322
Difficulty: Medium
Link: https://leetcode.com/problems/coin-change/

Problem Statement:
You are given an integer array coins representing different denominations
of coins and an integer amount representing a total amount of money.

Return the fewest number of coins needed to make up that amount.
If that amount cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Examples:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation:
11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1

Key Insight:
This is an **Unbounded Knapsack / Dynamic Programming** problem.
For each amount, determine the minimum coins needed.

Approach: Dynamic Programming (Bottom-Up)
-----------------------------------------
Let dp[x] = minimum number of coins needed to make amount x.

Steps:
1. Initialize dp array of size amount + 1:
   - dp[0] = 0
   - All other values = infinity (or amount + 1)
2. For each amount from 1 to amount:
   - For each coin in coins:
       - If coin <= current amount:
           dp[x] = min(dp[x], dp[x - coin] + 1)
3. If dp[amount] is still infinity, return -1.
   Otherwise, return dp[amount].

Time Complexity:
- O(amount × number_of_coins)

Space Complexity:
- O(amount)
"""

class Solution(object):
    def coinChange(self, coins, amount):
        # Initialize dp array
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for curr_amount in range(1, amount + 1):
            for coin in coins:
                if coin <= curr_amount:
                    dp[curr_amount] = min(
                        dp[curr_amount],
                        dp[curr_amount - coin] + 1
                    )

        return -1 if dp[amount] == amount + 1 else dp[amount]
