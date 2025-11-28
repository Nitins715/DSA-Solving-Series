"""
Problem: Find the Kth Largest Integer in the Array
LeetCode #1985
Difficulty: Medium
Link: https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

Problem Statement:
You are given an array nums of strings, where each string represents a non-negative integer.
Return the string that represents the **kth largest integer** in the array.

Important details:
- Integers may be too large to fit in 64-bit types.
- Sorting must be based on integer value, NOT string lexicographic order.
- Leading zeros should not affect value: "0012" == "12", but keep original string.

Example:
Input: nums = ["3","6","7","10"], k = 4
Sorted values: ["10","7","6","3"]
Output: "3"

Input: nums = ["2","21","12","1"], k = 3
Sorted values: ["21","12","2","1"]
Output: "2"

Input: nums = ["0","0"], k = 2
Output: "0"

Approach:
We want the kth largest integer.
Two ways:
1. Sort all numbers using custom comparator (O(n log n))
2. Use a min-heap of size k (O(n log k)) → more optimal

We use method #2:
- Convert each string to its integer-equivalent comparison:
    primary key: length of string  
    secondary key: lexicographic order  
  Because longer length → larger integer.

- Push items into min-heap of size k:
    Key: (length, string)
- If heap exceeds size k → pop smallest (i.e., smallest integer)
- After processing all numbers, heap[0] contains the kth largest.

Time Complexity:
- O(n log k)
Space Complexity:
- O(k)
"""

import heapq

class Solution(object):
    def kthLargestNumber(self, nums, k):
        minheap = []

        for num in nums:
            key = (len(num), num)  # Longer length → larger integer

            heapq.heappush(minheap, key)

            if len(minheap) > k:
                heapq.heappop(minheap)

        # kth largest integer is the smallest in the heap
        return minheap[0][1]
