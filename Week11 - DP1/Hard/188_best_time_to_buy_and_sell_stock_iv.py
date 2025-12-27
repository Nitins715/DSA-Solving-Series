"""
Problem: Best Time to Buy and Sell Stock IV
LeetCode #188
Difficulty: Hard
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

Problem Statement:
You are given an integer k and an array prices where prices[i] is the price
of a given stock on the i-th day.

You may complete at most k transactions.
Each transaction consists of buying and then selling one share of the stock.

You may not hold more than one share of the stock at a time.

Return the maximum profit you can achieve.

Examples:
Input: k = 2, prices = [2,4,1]
Output: 2

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7

Key Insight:
This is a **Dynamic Programming** problem with transaction limits.

If k >= n/2, the problem becomes equivalent to
Best Time to Buy and Sell Stock II (unlimited transactions).

Approach 1: Optimized Case (Unlimited Transactions)
---------------------------------------------------
If k >= len(prices) // 2:
- Sum all positive differences (greedy).

Approach 2: Dynamic Programming (Transaction States)
----------------------------------------------------
Let:
- buy[j]  = max profit after j-th buy
- sell[j] = max profit after j-th sell

Steps:
1. Initialize:
   - buy[j] = -infinity
   - sell[j] = 0
2. For each price:
   - For j from 1 to k:
       buy[j]  = max(buy[j],  sell[j-1] - price)
       sell[j] = max(sell[j], buy[j] + price)
3. Return sell[k]

Time Complexity:
- O(n × k)

Space Complexity:
- O(k)
"""

class Solution(object):
    def maxProfit(self, k, prices):
        n = len(prices)
        if n == 0 or k == 0:
            return 0

        # Optimization: unlimited transactions case
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

        buy = [float('-inf')] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:
            for j in range(1, k + 1):
                buy[j] = max(buy[j], sell[j - 1] - price)
                sell[j] = max(sell[j], buy[j] + price)

        return sell[k]
