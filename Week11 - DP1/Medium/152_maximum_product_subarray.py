# File Name: 152_maximum_product_subarray.py

"""
Problem: Maximum Product Subarray
LeetCode #152
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-product-subarray/

Problem Statement:
Given an integer array nums, find the contiguous subarray
within an array (containing at least one number)
which has the largest product.

Examples:
Input: nums = [2,3,-2,4]
Output: 6
Explanation:
The subarray [2,3] has the largest product = 6

Input: nums = [-2,0,-1]
Output: 0

Key Insight:
This is a **Dynamic Programming** problem.
Because of negative numbers, we must track:
- maximum product ending at current index
- minimum product ending at current index

A negative number can flip max ↔ min.

Approach: Dynamic Programming (Kadane-style)
--------------------------------------------
Steps:
1. Initialize:
   - max_prod = nums[0]
   - min_prod = nums[0]
   - result = nums[0]
2. Iterate from index 1 to end:
   - If nums[i] < 0, swap max_prod and min_prod
   - max_prod = max(nums[i], max_prod * nums[i])
   - min_prod = min(nums[i], min_prod * nums[i])
   - Update result
3. Return result

Time Complexity:
- O(n)

Space Complexity:
- O(1)
"""

class Solution(object):
    def maxProduct(self, nums):
        max_prod = nums[0]
        min_prod = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_prod, min_prod = min_prod, max_prod

            max_prod = max(nums[i], max_prod * nums[i])
            min_prod = min(nums[i], min_prod * nums[i])

            result = max(result, max_prod)

        return result
