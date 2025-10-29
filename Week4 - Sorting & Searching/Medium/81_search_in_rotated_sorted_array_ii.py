"""
Problem: Search in Rotated Sorted Array II  
LeetCode #81  
Difficulty: Medium  
Link: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/  

Problem Statement:  
There is an integer array nums sorted in non-decreasing order (not necessarily distinct values).  
Before being passed to your function, nums was rotated at an unknown pivot index k  
(such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], ..., nums[k-1]]).  

Given the array nums after rotation and an integer target,  
return true if target is in nums, or false if it is not in nums.  

You must decrease the overall runtime complexity as much as possible.  

Examples:  
Input: nums = [2,5,6,0,0,1,2], target = 0  
Output: True  

Input: nums = [2,5,6,0,0,1,2], target = 3  
Output: False  

Approach (Modified Binary Search with Duplicate Handling):  
- Similar to LeetCode #33 but includes handling duplicates.  
- Duplicates make it tricky to decide which half is sorted —  
  when nums[left] == nums[mid] == nums[right], simply shrink the search space by moving both ends.  
- Otherwise:
  - If left half is sorted:
    - Check if target lies in left range → move right = mid - 1.  
    - Else → move left = mid + 1.  
  - Else (right half is sorted):
    - Check if target lies in right range → move left = mid + 1.  
    - Else → move right = mid - 1.  

Time Complexity: O(log n) in average case, O(n) in worst case (due to duplicates)  
Space Complexity: O(1)
"""

class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return True
            
            # Handle duplicates
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            # Left half is sorted
            elif nums[left] <= nums[mid]:
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
        
        return False
