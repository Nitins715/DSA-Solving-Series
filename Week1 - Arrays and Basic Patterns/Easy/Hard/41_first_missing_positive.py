"""
Problem: First Missing Positive
LeetCode #41
Difficulty: Hard
Link: https://leetcode.com/problems/first-missing-positive/

Problem Statement:
Given an unsorted integer array nums, return the smallest missing positive integer.

Examples:
Input: nums = [1,2,0]
Output: 3

Approach:
- Place each number n in index n-1 position using swapping.
- Traverse array to find first index i where nums[i] != i+1; return i+1.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1
