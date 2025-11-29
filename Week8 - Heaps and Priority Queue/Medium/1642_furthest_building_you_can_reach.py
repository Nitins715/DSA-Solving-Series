"""
Problem: Furthest Building You Can Reach
LeetCode #1642
Difficulty: Medium
Link: https://leetcode.com/problems/furthest-building-you-can-reach/

Problem Statement:
You are given:
- heights[]: heights of buildings in order
- bricks: number of bricks you have
- ladders: number of ladders you can use

Rules for moving from building i → i+1:
- If next height <= current height → free move
- If next height > current:
      Let climb = next - current
      You must use either:
        • climb bricks, OR
        • 1 ladder (covers any height)

Goal:
Return the **furthest index** you can reach.

Example:
Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
Climbs:
 2→7 : 5
 6→9 : 3
 9→14: 5

Strategy:
- Use ladder on biggest climbs → bricks on smaller climbs.

Approach: Min-Heap of climbs
--------------------------------
We track all upward climbs in a min-heap:

Steps:
1. Iterate through buildings:
     - If heights[i+1] > heights[i], push climb into heap.
2. If heap size > ladders:
     - You must use bricks for the smallest climb → pop from heap.
3. If bricks < 0 at any time:
     - Can't progress, return previous index.

Why this works:
- We greedily assign ladders to biggest climbs by pushing climbs into heap and removing the smallest.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

import heapq

class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        heap = []  # min-heap

        for i in range(len(heights) - 1):
            diff = heights[i+1] - heights[i]

            if diff > 0:
                heapq.heappush(heap, diff)

            # If more climbs than ladders, use bricks on smallest climb
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)

            # If out of bricks → cannot move further
            if bricks < 0:
                return i

        return len(heights) - 1
