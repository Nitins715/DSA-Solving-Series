"""
Problem: Kth Largest Element in a Stream
LeetCode #703
Difficulty: Easy
Link: https://leetcode.com/problems/kth-largest-element-in-a-stream/

Problem Statement:
Design a class that finds the Kth largest element in a stream of numbers.
You are given:
- An integer k
- A list of integers nums
Your job is to implement:
- KthLargest.add(val): which adds val to the stream and returns the Kth largest element.

Example:
Input:
k = 3, nums = [4,5,8,2]

add(3) -> 4
add(5) -> 5
add(10) -> 5
add(9) -> 8
add(4) -> 8

Approach:
- Use a **min-heap** (priority queue) that always stores the k largest elements seen so far.
- The root of the heap (smallest element in heap) is always the current Kth largest value.
- Steps:
  1. Build a min-heap from nums.
  2. If its size exceeds k, pop until size becomes k.
  3. On each add(val):
     - Push val into heap.
     - If heap size > k, pop.
     - Return heap[0] (Kth largest).

Reason:
Min-heap of size k gives:
- O(log k) insertions
- O(1) access to Kth largest (heap[0])

Time Complexity:
- Building heap: O(n log k)
- Each add: O(log k)

Space Complexity:
- O(k)
"""

import heapq

class KthLargest(object):

    def __init__(self, k, nums):
        self.k = k
        self.minheap = nums
        heapq.heapify(self.minheap)

        # Maintain size k
        while len(self.minheap) > k:
            heapq.heappop(self.minheap)

    def add(self, val):
        heapq.heappush(self.minheap, val)
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]
