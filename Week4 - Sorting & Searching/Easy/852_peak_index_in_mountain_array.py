"""
Problem: Peak Index in a Mountain Array  
LeetCode #852  
Difficulty: Medium  
Link: https://leetcode.com/problems/peak-index-in-a-mountain-array/  

Problem Statement:  
An array arr is a mountain array if:  
- arr.length >= 3  
- There exists some i (0 < i < arr.length - 1) such that:  
  arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1]  

Given a mountain array arr, return the index i of the peak element.  

Examples:  
Input: arr = [0,1,0]  
Output: 1  

Input: arr = [0,2,1,0]  
Output: 1  

Input: arr = [0,10,5,2]  
Output: 1  

Approach (Binary Search):  
- The array strictly increases, then strictly decreases.  
- Use binary search:
  - mid = (left + right) // 2  
  - If arr[mid] < arr[mid + 1], the peak lies on the right side → left = mid + 1  
  - Else, the peak is at mid or to the left → right = mid  
- Continue until left == right → that index is the peak.  

Time Complexity: O(log n)  
Space Complexity: O(1)
"""

class Solution:
    def peakIndexInMountainArray(self, arr):
        left, right = 0, len(arr) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        
        return left
