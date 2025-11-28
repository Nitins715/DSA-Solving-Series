"""
Problem: Last Stone Weight
LeetCode #1046
Difficulty: Easy
Link: https://leetcode.com/problems/last-stone-weight/

Problem Statement:
You are given an array stones where stones[i] is the weight of the ith stone.

We repeatedly do the following:
- Select the two heaviest stones x and y (where x <= y).
- Smash them together:
  - If x == y, both stones are destroyed.
  - If x != y, the stone with weight x is destroyed, and the stone with weight y
    has new weight y - x.
- Continue this process until there is at most one stone left.

Return the weight of the last remaining stone.
If there are no stones left, return 0.

Examples:
Input: stones = [2,7,4,1,8,1]
Process:
- Take 7 and 8 -> smash -> new stone 1, stones = [2,4,1,1,1]
- Take 4 and 2 -> smash -> new stone 2, stones = [2,1,1,1]
- Take 2 and 1 -> smash -> new stone 1, stones = [1,1,1]
- Take 1 and 1 -> smash -> new stone 0 (both removed), stones = [1]
Output: 1

Input: stones = [1]
Output: 1

Approach:
- We need to repeatedly extract the two largest stones.
- The most efficient data structure to support this is a heap.
- Python's heapq is a **min-heap**, but we need a **max-heap** behavior:
  - Store negative values of stones to simulate a max-heap.
  - The "largest" stone will be the smallest negative number.

Steps:
1. Convert all stones to negative and push into a heap.
2. While heap size > 1:
   - Pop the two smallest (i.e., two largest original stones): y, x.
   - If x != y:
       - Compute new stone = y - x (both are negative, so difference still negative).
       - Push the new stone back into the heap.
3. If heap is empty, return 0.
   Otherwise, return the absolute value of the last element (negate it).

Time Complexity:
- Building the heap: O(n)
- Each smash operation: O(log n)
- In the worst case, we might do O(n) smash operations.
- Overall Time: O(n log n)

Space Complexity:
- O(n) for the heap.
"""

import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        # Convert to a max-heap by pushing negative values
        maxheap = [-s for s in stones]
        heapq.heapify(maxheap)

        while len(maxheap) > 1:
            # Pop two heaviest stones (largest -> smallest negative)
            y = heapq.heappop(maxheap)  # heaviest
            x = heapq.heappop(maxheap)  # second heaviest

            if x != y:
                # New stone weight (still negative)
                new_stone = y - x
                heapq.heappush(maxheap, new_stone)

        # If no stones left
        if not maxheap:
            return 0

        # Return positive weight of last stone
        return -maxheap[0]
