"""
Problem: Best Time to Buy and Sell Stock with Transaction Fee
LeetCode #714
Difficulty: Medium
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

Problem Statement:
You are given an array prices where prices[i] is the price of a given stock
on the i-th day, and an integer fee representing a transaction fee.

You may complete as many transactions as you like, but you must pay the
transaction fee for each transaction.

You may not hold more than one share of the stock at a time.

Return the maximum profit you can achieve.

Examples:
Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation:
- Buy at 1, sell at 8 → profit = 5
- Buy at 4, sell at 9 → profit = 3
Total profit = 8

Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6

Key Insight:
This is a **Dynamic Programming** problem with two states:
- hold: max profit when holding a stock
- cash: max profit when not holding a stock

Approach: Dynamic Programming (State Machine)
---------------------------------------------
At each day i:
- cash[i] = max(cash[i-1], hold[i-1] + prices[i] - fee)
- hold[i] = max(hold[i-1], cash[i-1] - prices[i])

We can optimize space to use two variables.

Steps:
1. Initialize:
   - cash = 0
   - hold = -prices[0]
2. For each price in prices:
   - Update cash and hold using the recurrence relations.
3. Return cash (profit when not holding any stock).

Time Complexity:
- O(n)

Space Complexity:
- O(1)
"""

class Solution(object):
    def maxProfit(self, prices, fee):
        cash = 0          # max profit when not holding stock
        hold = -prices[0] # max profit when holding stock

        for price in prices[1:]:
            cash = max(cash, hold + price - fee)
            hold = max(hold, cash - price)

        return cash
