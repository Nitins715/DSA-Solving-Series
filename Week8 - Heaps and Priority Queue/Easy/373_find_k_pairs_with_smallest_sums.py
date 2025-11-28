"""
Problem: Find K Pairs with Smallest Sums
LeetCode #373
Difficulty: Medium
Link: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

Problem Statement:
You are given two integer arrays nums1 and nums2 sorted in ascending order.
Return the k pairs (u, v) such that:
- u belongs to nums1
- v belongs to nums2
and the sum u + v is the smallest possible.

Example:
Input:
nums1 = [1,7,11], nums2 = [2,4,6], k = 3

Possible pairs by sum:
(1,2) -> 3
(1,4) -> 5
(1,6) -> 7
(7,2) -> 9
(7,4) -> 11
...
Smallest 3 → [(1,2), (1,4), (1,6)]

Input:
nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [(1,1), (1,1)]

Input:
nums1 = [1,2], nums2 = [3], k = 3
Output: [(1,3), (2,3)]

Approach:
- Since both arrays are sorted, the smallest possible sum must start from:
  (nums1[0], nums2[0]), (nums1[1], nums2[0]), (nums1[2], nums2[0]) ...
- Use a **min-heap** to always extract the next smallest pair.
- Push initial k candidates:
    (nums1[i] + nums2[0], i, 0)
- For each extracted pair (i,j):
    - Add result: (nums1[i], nums2[j])
    - Push the next pair from nums2: (i, j+1) if exists.

This avoids generating all n*m pairs.

Time Complexity:
- O(k log k) because heap never grows larger than k.
Space Complexity:
- O(k) for heap and result.
"""

import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2 or k == 0:
            return []

        minheap = []
        result = []

        # Push first element of nums2 paired with first k elements of nums1
        for i in range(min(k, len(nums1))):
            heapq.heappush(minheap, (nums1[i] + nums2[0], i, 0))

        while minheap and len(result) < k:
            total, i, j = heapq.heappop(minheap)
            result.append([nums1[i], nums2[j]])

            # Push next pair with nums2[j+1]
            if j + 1 < len(nums2):
                heapq.heappush(minheap, (nums1[i] + nums2[j+1], i, j+1))

        return result
