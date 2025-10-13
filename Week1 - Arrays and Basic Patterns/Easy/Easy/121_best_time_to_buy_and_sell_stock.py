"""
Problem: Best Time to Buy and Sell Stock
LeetCode #121
Difficulty: Easy
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Problem Statement:
Given prices of a stock, choose a single day to buy and another day to sell to maximize profit.

Examples:
Input: prices = [7,1,5,3,6,4]
Output: 5

Approach:
- Track minimum price and maximum profit while iterating.
- For each price, profit = price - min_price
- Update max_profit if profit is higher.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
