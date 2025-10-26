"""
Problem: Binary Search  
LeetCode #704  
Difficulty: Easy  
Link: https://leetcode.com/problems/binary-search/  

Problem Statement:  
Given an array of integers nums which is sorted in ascending order,  
and an integer target, write a function to search target in nums.  
If target exists, return its index. Otherwise, return -1.  

You must write an algorithm with O(log n) runtime complexity.

Examples:  
Input: nums = [-1,0,3,5,9,12], target = 9  
Output: 4  

Input: nums = [-1,0,3,5,9,12], target = 2  
Output: -1  

Approach (Binary Search):  
- Initialize two pointers: left = 0 and right = len(nums) - 1.  
- While left <= right:
  - Find mid = (left + right) // 2.  
  - If nums[mid] == target → return mid.  
  - If nums[mid] < target → move left = mid + 1.  
  - Else → move right = mid - 1.  
- If target not found, return -1.  

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
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
