"""
Problem: Find Median from Data Stream
LeetCode #295
Difficulty: Hard
Link: https://leetcode.com/problems/find-median-from-data-stream/

Problem Statement:
Design a data structure to support:
- addNum(num): Add a number into the data stream.
- findMedian(): Return the median of all numbers so far.

Constraints:
- You must achieve efficient operations:
      addNum → O(log n)
      findMedian → O(1)

Examples:
Input:
addNum(1)
addNum(2)
findMedian() → 1.5
addNum(3)
findMedian() → 2

Approach: Two Heaps (Max-Heap + Min-Heap)
-----------------------------------------
Use:
- Max-heap `low`  → keeps the *smaller* half of numbers
- Min-heap `high` → keeps the *larger* half of numbers

Goals:
1. All values in `low` ≤ all values in `high`
2. Size difference between the heaps should be at most 1.

Steps for addNum(x):
1. Push x into max-heap `low` (as negative to simulate max-heap)
2. Move the largest of low to high to maintain ordering
3. If heaps unbalanced (low has fewer elements), move top of high to low

Median:
- If heaps sizes equal → median = (top(low) + top(high)) / 2
- Else → median = top of the larger heap (low)

This ensures O(log n) insertion and O(1) median lookup.

Time Complexity:
- addNum: O(log n)
- findMedian: O(1)

Space Complexity:
- O(n)
"""

import heapq

class MedianFinder(object):

    def __init__(self):
        self.low = []   # max-heap (store as negative numbers)
        self.high = []  # min-heap

    def addNum(self, num):
        # Step 1: push to max-heap (low)
        heapq.heappush(self.low, -num)

        # Step 2: ensure ordering → largest of low must go to high
        val = -heapq.heappop(self.low)
        heapq.heappush(self.high, val)

        # Step 3: balance heaps → low should be equal or 1 bigger
        if len(self.high) > len(self.low):
            val = heapq.heappop(self.high)
            heapq.heappush(self.low, -val)

    def findMedian(self):
        # If sizes equal: average
        if len(self.low) == len(self.high):
            return (-self.low[0] + self.high[0]) / 2.0
        # Else low has one extra
        return -self.low[0]
