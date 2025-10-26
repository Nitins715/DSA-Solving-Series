"""
Problem: Squares of a Sorted Array  
LeetCode #977  
Difficulty: Easy  
Link: https://leetcode.com/problems/squares-of-a-sorted-array/  

Problem Statement:  
Given an integer array nums sorted in non-decreasing order,  
return an array of the squares of each number sorted in non-decreasing order.  

Examples:  
Input: nums = [-4,-1,0,3,10]  
Output: [0,1,9,16,100]  

Input: nums = [-7,-3,2,3,11]  
Output: [4,9,9,49,121]  

Approach (Two-Pointer Technique):  
- Since the array is sorted, the largest square will come from  
  either the leftmost (negative) or rightmost (positive) value.  
- Use two pointers:
  - left = 0  
  - right = len(nums) - 1  
- Compare abs(nums[left]) and abs(nums[right]) and append the larger square  
  to the result (in reverse order).  
- Finally, reverse the result list.  

Time Complexity: O(n)  
Space Complexity: O(n)
"""

class Solution:
    def sortedSquares(self, nums):
        left, right = 0, len(nums) - 1
        result = []
        
        while left <= right:
            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]
            
            if left_square > right_square:
                result.append(left_square)
                left += 1
            else:
                result.append(right_square)
                right -= 1
        
        return result[::-1]
