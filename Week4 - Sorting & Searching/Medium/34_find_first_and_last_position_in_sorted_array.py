"""
Problem: Find First and Last Position of Element in Sorted Array  
LeetCode #34  
Difficulty: Medium  
Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/  

Problem Statement:  
Given an array of integers nums sorted in non-decreasing order,  
find the starting and ending position of a given target value.  

If target is not found in the array, return [-1, -1].  

You must write an algorithm with O(log n) runtime complexity.  

Examples:  
Input: nums = [5,7,7,8,8,10], target = 8  
Output: [3,4]  

Input: nums = [5,7,7,8,8,10], target = 6  
Output: [-1,-1]  

Input: nums = [], target = 0  
Output: [-1,-1]  

Approach (Binary Search for First and Last Occurrence):  
- Use binary search twice:  
  1️⃣ To find the first occurrence (move `right` leftward when target found).  
  2️⃣ To find the last occurrence (move `left` rightward when target found).  
- If target not found → return [-1, -1].  

Time Complexity: O(log n)  
Space Complexity: O(1)
"""

class Solution:
    def searchRange(self, nums, target):
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            first = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    first = mid
                    right = mid - 1  # look for earlier occurrence
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return first

        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            last = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    last = mid
                    left = mid + 1  # look for later occurrence
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return last

        first = findFirst(nums, target)
        last = findLast(nums, target)
        return [first, last]
