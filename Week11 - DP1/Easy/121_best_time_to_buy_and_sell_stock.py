# File Name: 121_best_time_to_buy_and_sell_stock.py

"""
Problem: Best Time to Buy and Sell Stock
LeetCode #121
Difficulty: Easy
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Problem Statement:
You are given an array prices where prices[i] is the price of a given stock
on the i-th day.

You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve.
If you cannot achieve any profit, return 0.

Examples:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation:
- Buy on day 2 (price = 1)
- Sell on day 5 (price = 6)
Profit = 6 - 1 = 5

Input: prices = [7,6,4,3,1]
Output: 0
Explanation:
- No profitable transaction possible

Key Insight:
This is a **Greedy / Dynamic Programming** problem.
At each day, track:
- the minimum price seen so far (best day to buy)
- the maximum profit achievable if selling today

Approach: One-Pass Greedy
------------------------
Steps:
1. Initialize:
   - min_price = infinity
   - max_profit = 0
2. Iterate through prices:
   - Update min_price if current price is lower
   - Calculate profit = current price - min_price
   - Update max_profit if profit is higher
3. Return max_profit

Time Complexity:
- O(n)

Space Complexity:
- O(1)
"""

class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit
