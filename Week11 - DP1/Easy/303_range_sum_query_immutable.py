# File Name: 303_range_sum_query_immutable.py

"""
Problem: Range Sum Query - Immutable
LeetCode #303
Difficulty: Easy
Link: https://leetcode.com/problems/range-sum-query-immutable/

Problem Statement:
Given an integer array nums, handle multiple queries of the following type:
- Calculate the sum of the elements of nums between indices left and right inclusive
  where left <= right.

Implement the NumArray class:
- NumArray(int[] nums) initializes the object with the integer array nums
- int sumRange(int left, int right) returns the sum of elements between indices
  left and right inclusive

Key Insight:
This problem is best solved using a **Prefix Sum** array.
Once prefix sums are built, each range sum query can be answered in O(1) time.

Prefix Sum Definition:
prefix[i] = sum of elements from index 0 to index i-1

Approach: Prefix Sum
--------------------
Steps:
1. Build a prefix sum array of size n + 1.
2. prefix[0] = 0
3. prefix[i] = prefix[i - 1] + nums[i - 1]
4. To compute sumRange(left, right):
   - return prefix[right + 1] - prefix[left]

Time Complexity:
- Preprocessing: O(n)
- Each Query: O(1)

Space Complexity:
- O(n)
"""

class NumArray(object):
    def __init__(self, nums):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]
