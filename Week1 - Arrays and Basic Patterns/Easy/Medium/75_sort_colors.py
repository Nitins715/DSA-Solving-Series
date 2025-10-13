"""
Problem: Sort Colors
LeetCode #75
Difficulty: Medium
Link: https://leetcode.com/problems/sort-colors/

Problem Statement:
Given an array nums with n objects colored red, white, or blue (represented by 0, 1, 2), sort them in-place 
so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

Examples:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Approach:
- Use Dutch National Flag algorithm:
  - Three pointers: low, mid, high.
  - Swap elements to correct position in one pass.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def sortColors(self, nums):
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
