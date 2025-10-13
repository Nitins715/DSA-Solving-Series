"""
Problem: Remove Duplicates from Sorted Array
LeetCode #26
Difficulty: Easy
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Problem Statement:
Given a sorted array nums, remove duplicates in-place such that each element appears only once. 
Return the new length. Modify the array in-place.

Examples:
Input: nums = [1,1,2]
Output: Length: 2, Array: [1,2]

Approach:
- Use two pointers:
  - k points to next unique element.
  - Traverse array from index 1.
  - If nums[i] != nums[i-1], nums[k] = nums[i], increment k.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k
