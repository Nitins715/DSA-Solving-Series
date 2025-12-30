"""
Problem: Min Cost Climbing Stairs
LeetCode #746
Difficulty: Easy
Link: https://leetcode.com/problems/min-cost-climbing-stairs/

Problem Statement:
You are given an integer array cost where cost[i] is the cost of the i-th step.
Once you pay the cost, you can either climb one or two steps.

You can either start from step 0 or step 1.
Return the minimum cost to reach the top of the floor.

The top of the floor is beyond the last index of the array.

Examples:
Input: cost = [10,15,20]
Output: 15

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6

Key Insight:
This is a **Dynamic Programming** problem.

To reach step i, the minimum cost is:
- from step i-1
- from step i-2

Approach: Dynamic Programming (Space Optimized)
-----------------------------------------------
Let:
- prev2 = min cost to reach step i-2
- prev1 = min cost to reach step i-1

Steps:
1. Initialize prev2 = 0, prev1 = 0
2. For i from 2 to n:
   - curr = min(prev1 + cost[i-1], prev2 + cost[i-2])
3. Slide window forward.
4. Return prev1 (cost to reach the top).

Time Complexity:
- O(n)

Space Complexity:
- O(1)
"""

class Solution(object):
    def minCostClimbingStairs(self, cost):
        prev2 = 0
        prev1 = 0

        for i in range(2, len(cost) + 1):
            curr = min(prev1 + cost[i - 1], prev2 + cost[i - 2])
            prev2 = prev1
            prev1 = curr

        return prev1
