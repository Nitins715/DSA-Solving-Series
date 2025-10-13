"""
Problem: Maximum Subarray
LeetCode #53
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-subarray/

Problem Statement:
Given an integer array nums, find the contiguous subarray which has the largest sum and return its sum.

Examples:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6

Approach:
- Use Kadane's algorithm:
  - Initialize current_sum and max_sum.
  - For each element, current_sum = max(num, current_sum+num)
  - Update max_sum = max(max_sum, current_sum)

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def maxSubArray(self, nums):
        max_sum = current_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum