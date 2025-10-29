"""
Problem: Find Minimum in Rotated Sorted Array  
LeetCode #153  
Difficulty: Medium  
Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/  

Problem Statement:  
Suppose an array of length n sorted in ascending order is rotated between 1 and n times.  
For example, the array nums = [0,1,2,4,5,6,7] might become:  
- [4,5,6,7,0,1,2] if it was rotated 4 times.  

Return the minimum element of this array.  
You must write an algorithm with O(log n) runtime complexity.  

Examples:  
Input: nums = [3,4,5,1,2]  
Output: 1  

Input: nums = [4,5,6,7,0,1,2]  
Output: 0  

Input: nums = [11,13,15,17]  
Output: 11  

Approach (Binary Search):  
- The minimum element is the rotation point — where the order breaks.  
- Use binary search:
  - If nums[mid] > nums[right], the minimum is in the right half → left = mid + 1.  
  - Else → minimum is in the left half (including mid) → right = mid.  
- Continue until left == right, and return nums[left].  

Time Complexity: O(log n)  
Space Complexity: O(1)
"""

class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If mid element > rightmost, min must be in right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid  # min could be mid or to its left
        
        return nums[left]
