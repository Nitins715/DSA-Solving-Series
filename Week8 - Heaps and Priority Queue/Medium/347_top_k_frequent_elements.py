"""
Problem: Top K Frequent Elements
LeetCode #347
Difficulty: Medium
Link: https://leetcode.com/problems/top-k-frequent-elements/

Problem Statement:
Given an integer array nums and an integer k, return the k most frequent elements.
The answer may be returned in any order.

Example:
Input: nums = [1,1,1,2,2,3], k = 2
Frequencies:
    1 -> 3
    2 -> 2
    3 -> 1
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]

Approach:
We want the k most frequent elements.
Two common approaches:
1. Sort by frequency → O(n log n)
2. Use a **min-heap** of size k → O(n log k) (better)

We use method #2:
- Count frequencies with Counter
- Push (frequency, value) into a min-heap
- If heap size exceeds k, pop the smallest frequency
- Remaining elements in the heap are the k most frequent

Time Complexity:
- Counting: O(n)
- Heap operations: O(n log k)
- Overall: O(n log k)

Space Complexity:
- O(n) for frequency map
- O(k) for heap
"""

import heapq
from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        freq = Counter(nums)
        minheap = []

        for num, count in freq.items():
            heapq.heappush(minheap, (count, num))
            if len(minheap) > k:
                heapq.heappop(minheap)

        # Extract elements (only the numbers)
        return [num for (count, num) in minheap]
