"""
Problem: Search Insert Position  
LeetCode #35  
Difficulty: Easy  
Link: https://leetcode.com/problems/search-insert-position/  

Problem Statement:  
Given a sorted array of distinct integers and a target value,  
return the index if the target is found.  
If not, return the index where it would be if it were inserted in order.  

You must write an algorithm with O(log n) runtime complexity.

Examples:  
Input: nums = [1,3,5,6], target = 5  
Output: 2  

Input: nums = [1,3,5,6], target = 2  
Output: 1  

Input: nums = [1,3,5,6], target = 7  
Output: 4  

Approach (Binary Search):  
- Initialize left = 0 and right = len(nums) - 1.  
- Perform binary search:
  - If nums[mid] == target → return mid.  
  - If nums[mid] < target → move left = mid + 1.  
  - Else → move right = mid - 1.  
- If target is not found, the correct insert position is `left` (where it would fit).  

Time Complexity: O(log n)  
Space Complexity: O(1)
"""

class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left
