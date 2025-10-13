"""
Problem: Product of Array Except Self
LeetCode #238
Difficulty: Medium
Link: https://leetcode.com/problems/product-of-array-except-self/

Problem Statement:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements 
of nums except nums[i]. Solve it without using division and in O(n).

Examples:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Approach:
- Use two passes:
  - First pass: compute prefix product for each index.
  - Second pass: compute suffix product in reverse and multiply with prefix.

Time Complexity: O(n)
Space Complexity: O(1) extra space (output array not counted)
"""

class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        output = [1] * n

        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n-1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output
