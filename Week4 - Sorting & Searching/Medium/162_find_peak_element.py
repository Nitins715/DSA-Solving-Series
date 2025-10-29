"""
Problem: Find Peak Element  
LeetCode #162  
Difficulty: Medium  
Link: https://leetcode.com/problems/find-peak-element/  

Problem Statement:  
A peak element is an element that is strictly greater than its neighbors.  
Given an integer array nums, find a peak element and return its index.  

If the array contains multiple peaks, return the index of any one of them.  
You may imagine that nums[-1] = nums[n] = -∞ (i.e., virtual boundaries).  

Examples:  
Input: nums = [1,2,3,1]  
Output: 2  

Input: nums = [1,2,1,3,5,6,4]  
Output: 5  
Explanation: Both 2 and 5 are valid answers.  

Approach (Binary Search):  
- Use binary search to find a peak element efficiently.  
- Compare the middle element with its right neighbor:  
  - If nums[mid] > nums[mid + 1] → peak is on the left side (including mid).  
  - Else → peak is on the right side.  
- Continue until left == right → return left (or right).  

Time Complexity: O(log n)  
Space Complexity: O(1)
"""

class Solution:
    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[mid + 1]:
                right = mid  # peak is in the left half (including mid)
            else:
                left = mid + 1  # peak is in the right half
        
        return left
