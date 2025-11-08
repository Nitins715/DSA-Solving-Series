"""
Problem: Final Prices With a Special Discount in a Shop
LeetCode #1475
Difficulty: Easy
Link: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

Problem Statement:
You are given an integer array prices where prices[i] is the price of the ith item in a shop.
There is a special discount for each item:
You will receive a discount equal to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i].
If no such j exists, you will not receive any discount at all.

Return an integer array where the ith element is the final price you will pay for the ith item of the shop.

Examples:
Input: prices = [8,4,6,2,3]
Output: [4,2,4,2,3]
Explanation: 
- For item 0, prices[1] = 4 is the first smaller or equal price → discount 4 → 8 - 4 = 4
- For item 1, prices[3] = 2 → 4 - 2 = 2
- For item 2, prices[3] = 2 → 6 - 2 = 4
- For item 3, no smaller → 2
- For item 4, no smaller → 3

Input: prices = [1,2,3,4,5]
Output: [1,2,3,4,5]

Input: prices = [10,1,1,6]
Output: [9,0,1,6]

Approach:
- Use a stack to efficiently find the next smaller or equal element for each price.
- Traverse from left to right:
  - While stack not empty and current price <= price at stack top:
    - Apply discount and pop from stack.
  - Push current index onto stack.
- Return updated prices array.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def finalPrices(self, prices):
        stack = []  # Stack to store indices
        for i in range(len(prices)):
            # Apply discount when a smaller or equal price is found
            while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()
                prices[idx] -= prices[i]
            stack.append(i)
        return prices
