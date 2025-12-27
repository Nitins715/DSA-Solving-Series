# File Name: 122_best_time_to_buy_and_sell_stock_ii.py

"""
Problem: Best Time to Buy and Sell Stock II
LeetCode #122
Difficulty: Medium
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Problem Statement:
You are given an array prices where prices[i] is the price of a given stock
on the i-th day.

You are allowed to complete as many transactions as you like
(i.e., buy one and sell one share of the stock multiple times).
However, you may not hold more than one share of the stock at a time.

Return the maximum profit you can achieve.

Examples:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation:
- Buy on day 2 (price = 1), sell on day 3 (price = 5), profit = 4
- Buy on day 4 (price = 3), sell on day 5 (price = 6), profit = 3
Total profit = 7

Input: prices = [1,2,3,4,5]
Output: 4
Explanation:
- Buy on day 1, sell on day 5
(or equivalently, sum of daily increases)

Key Insight:
This is a **Greedy** problem.
Any time there is a price increase from one day to the next,
you can take that profit.

Approach: Greedy (Sum of Positive Differences)
----------------------------------------------
Steps:
1. Initialize total_profit = 0
2. Iterate from day 1 to end:
   - If prices[i] > prices[i-1]:
       add prices[i] - prices[i-1] to total_profit
3. Return total_profit

Time Complexity:
- O(n)

Space Complexity:
- O(1)
"""

class Solution(object):
    def maxProfit(self, prices):
        total_profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                total_profit += prices[i] - prices[i - 1]

        return total_profit
