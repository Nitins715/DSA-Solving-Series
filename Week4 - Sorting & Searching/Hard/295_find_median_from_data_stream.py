"""
Problem: Find Median from Data Stream  
LeetCode #295  
Difficulty: Hard  
Link: https://leetcode.com/problems/find-median-from-data-stream/  

Problem Statement:  
The MedianFinder class should support:
- addNum(int num): adds the integer num from the data stream to the data structure.  
- findMedian(): returns the median of all elements so far.  

The median is the middle value in an ordered integer list.  
If the size is even, the median is the average of the two middle values.  

Examples:  
Input:
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]  
[[], [1], [2], [], [3], []]  
Output:
[None, None, None, 1.5, None, 2.0]

Approach (Two Heaps):  
- Maintain two heaps:
  - A **max-heap (left)** for the smaller half of numbers.  
  - A **min-heap (right)** for the larger half.  
- Balancing:
  - After adding a number, make sure the size difference ≤ 1.  
  - If max-heap has more elements → move top to min-heap, and vice versa.  
- Median:
  - If sizes equal → average of both tops.  
  - If unequal → top of the larger heap.

Time Complexity:  
- addNum(): O(log n)  
- findMedian(): O(1)  

Space Complexity: O(n)
"""

import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # max-heap (store as negative values)
        self.large = []  # min-heap

    def addNum(self, num):
        # Step 1: Add to max heap (invert sign for max behavior)
        heapq.heappush(self.small, -num)

        # Step 2: Balance by ensuring all elements in small <= large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Step 3: Balance heap sizes (difference <= 1)
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2
