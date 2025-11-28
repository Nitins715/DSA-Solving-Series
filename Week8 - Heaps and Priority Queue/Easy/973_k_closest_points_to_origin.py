"""
Problem: K Closest Points to Origin
LeetCode #973
Difficulty: Medium
Link: https://leetcode.com/problems/k-closest-points-to-origin/

Problem Statement:
Given an array points where points[i] = [x_i, y_i],
return the k closest points to the origin (0,0).

Distance Formula:
Distance = sqrt(x^2 + y^2)
But since sqrt is monotonic, we can compare using x^2 + y^2 directly.

Example:
Input: points = [[1,3],[-2,2]], k = 1
Distances:
  [1,3]  -> 10
  [-2,2] -> 8
Closest → [-2,2]

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Distances:
  [3,3]  -> 18
  [5,-1] -> 26
  [-2,4] -> 20
Closest → [[3,3], [-2,4]]

Approach:
We need k smallest distances.
Two main methods:
1. **Min-heap with all points** (O(n log n))
2. **Max-heap of size k** (optimal → O(n log k))

We use method #2:
- Push (negative distance, point) so we maintain a max-heap of size k.
- If heap grows beyond k, pop the farthest point.
- Remaining items in heap are the k closest points.

Time Complexity:
- O(n log k) because heap never exceeds size k.

Space Complexity:
- O(k) for heap.
"""

import heapq

class Solution(object):
    def kClosest(self, points, k):
        maxheap = []

        for x, y in points:
            dist = x*x + y*y
            # Push negative distance to simulate max-heap
            heapq.heappush(maxheap, (-dist, x, y))

            # If more than k, remove farthest point
            if len(maxheap) > k:
                heapq.heappop(maxheap)

        # Extract just points
        return [[x, y] for (_, x, y) in maxheap]
