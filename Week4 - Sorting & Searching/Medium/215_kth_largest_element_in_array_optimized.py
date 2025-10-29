"""
Problem: Kth Largest Element in an Array  
LeetCode #215  
Difficulty: Medium  
Link: https://leetcode.com/problems/kth-largest-element-in-an-array/  

Problem Statement:  
Given an integer array nums and an integer k,  
return the kth largest element in the array.  

Note: It is the kth largest element in sorted order,  
not the kth distinct element.  

Examples:  
Input: nums = [3,2,1,5,6,4], k = 2  
Output: 5  

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4  
Output: 4  

Optimized Approach (Min-Heap):  
- Use a **min-heap** of size k to keep track of the k largest elements seen so far.  
- Iterate through nums:
  - Push each element into the heap.  
  - If heap size exceeds k, pop the smallest element.  
- After processing all elements, the heap root (top) is the kth largest element.  

This is the most **LeetCode-optimized** approach because:
- It’s simple, reliable, and avoids Quickselect’s worst-case O(n²).
- Runs fast in practice due to heapq’s efficient C implementation.

Time Complexity: O(n log k)  
Space Complexity: O(k)
"""

import heapq

class Solution:
    def findKthLargest(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
