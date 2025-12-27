"""
Problem: Maximum Subarray
LeetCode #53
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-subarray/

Problem Statement:
Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum
and return its sum.

Examples:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation:
The subarray [4,-1,2,1] has the largest sum = 6

Input: nums = [1]
Output: 1

Key Insight:
This problem is solved using **Kadane’s Algorithm**.

At each index, decide:
- Extend the current subarray
- Or start a new subarray at the current element

Approach: Kadane’s Algorithm
----------------------------
Steps:
1. Initialize:
   - current_sum = nums[0]
   - max_sum = nums[0]
2. Iterate from index 1 to end:
   - current_sum = max(nums[i], current_sum + nums[i])
   - max_sum = max(max_sum, current_sum)
3. Return max_sum

Time Complexity:
- O(n)

Space Complexity:
- O(1)
"""

class Solution(object):
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum
