"""
Problem: Kth Largest Element in an Array
LeetCode #215
Difficulty: Medium
Link: https://leetcode.com/problems/kth-largest-element-in-an-array/

Problem Statement:
Given an integer array nums and an integer k, return the kth largest element in the array.
Note:
- Kth largest means sorted in descending order.
- Example: 1st largest = max element.

Examples:
Input: nums = [3,2,1,5,6,4], k = 2
Sorted descending: [6,5,4,3,2,1]
Output: 5

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Sorted descending: [6,5,5,4,3,3,2,2,1]
Output: 4

Approach:
Use a **min-heap** of size k (optimal):
- Push each element into the heap.
- If heap grows larger than k, remove smallest element.
- After processing all elements:
    - heap[0] = kth largest.

Reasoning:
- We only keep track of the top k largest elements.
- Min-heap ensures heap[0] is always the smallest among the top k largest.

Time Complexity:
- O(n log k)

Space Complexity:
- O(k)
"""

import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        minheap = []

        for num in nums:
            heapq.heappush(minheap, num)
            if len(minheap) > k:
                heapq.heappop(minheap)

        return minheap[0]
