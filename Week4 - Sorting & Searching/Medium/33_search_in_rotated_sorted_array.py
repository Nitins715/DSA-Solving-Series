"""
Problem: Search in Rotated Sorted Array  
LeetCode #33  
Difficulty: Medium  
Link: https://leetcode.com/problems/search-in-rotated-sorted-array/  

Problem Statement:  
There is an integer array nums sorted in ascending order (with distinct values).  
Prior to being passed to your function, nums was rotated at an unknown pivot index k  
(such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], ..., nums[k-1]]).  

Given the array nums after rotation and an integer target,  
return the index of target if it is in nums, or -1 if it is not in nums.  

You must write an algorithm with O(log n) runtime complexity.  

Examples:  
Input: nums = [4,5,6,7,0,1,2], target = 0  
Output: 4  

Input: nums = [4,5,6,7,0,1,2], target = 3  
Output: -1  

Input: nums = [1], target = 0  
Output: -1  

Approach (Modified Binary Search):  
- Even though the array is rotated, one half (left or right) is always sorted.  
- Use binary search:
  - Check if nums[mid] == target → return mid.  
  - If left half is sorted (nums[left] <= nums[mid]):
    - If target is within this half → move right = mid - 1.  
    - Else → move left = mid + 1.  
  - Else (right half is sorted):
    - If target is within this half → move left = mid + 1.  
    - Else → move right = mid - 1.  

Time Complexity: O(log n)  
Space Complexity: O(1)
"""

class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1
