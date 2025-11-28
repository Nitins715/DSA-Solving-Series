"""
Problem: IPO
LeetCode #502
Difficulty: Hard
Link: https://leetcode.com/problems/ipo/

Problem Statement:
You are given:
- An integer k (maximum number of projects you can complete)
- An integer w (initial capital)
- Arrays profits[i] and capital[i], each describing:
    • profit gained from project i
    • minimum capital required to start project i

Goal:
Maximize your total capital after completing at most k projects.

Rules:
- You can only start a project if your current capital ≥ project’s required capital.
- After completing a project, your capital increases by its profit.
- Choose projects optimally to maximize capital.

Example:
Input:
k = 2, w = 0
profits = [1,2,3]
capital = [0,1,1]

Step-by-step:
- Initially capital = 0 → only project 0 is affordable (profit 1).
- Do project 0 → capital = 1
- Now affordable: project 1 (profit 2), project 2 (profit 3)
- Choose max-profit project = 3 → capital = 4
Output: 4

Approach:
Use two heaps:
1. Min-heap sorted by capital (projects locked until affordable)
2. Max-heap sorted by profit (projects you can choose now)

Algorithm:
- Push all projects into a min-heap as (capital_required, profit).
- For up to k iterations:
    • Move all projects whose required capital ≤ current w into a max-heap.
    • If max-heap is empty → cannot do any more projects → return w.
    • Pop the project with the highest profit from max-heap and add its profit to w.

Why heaps?
- Min-heap quickly finds which projects become affordable.
- Max-heap picks the most profitable among affordable ones.

Time Complexity:
- Building heaps: O(n)
- Each iteration: O(log n)
Overall: O(n log n)

Space Complexity:
- O(n) for heaps
"""

import heapq

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        n = len(profits)

        # Min-heap for locked projects (capital required)
        min_cap_heap = []
        for i in range(n):
            heapq.heappush(min_cap_heap, (capital[i], profits[i]))

        # Max-heap for affordable projects
        max_profit_heap = []

        for _ in range(k):
            # Move all affordable projects to max heap
            while min_cap_heap and min_cap_heap[0][0] <= w:
                cap, prof = heapq.heappop(min_cap_heap)
                heapq.heappush(max_profit_heap, -prof)  # Using negative for max-heap

            # If no affordable project → stop
            if not max_profit_heap:
                return w

            # Choose project with maximum profit
            w += -heapq.heappop(max_profit_heap)

        return w
