"""
Problem: Single Number  
LeetCode #136  
Difficulty: Easy  
Link: https://leetcode.com/problems/single-number/  

Problem Statement:  
Given a non-empty array of integers nums, every element appears twice except for one.  
Find that single one.  
You must implement a solution with a linear runtime complexity and use only constant extra space.

Examples:  
Input: nums = [2,2,1]  
Output: 1  

Input: nums = [4,1,2,1,2]  
Output: 4  

Input: nums = [1]  
Output: 1  

Approach (Bitwise XOR):  
- Initialize a variable `result` to 0.  
- Iterate through each number in nums and apply XOR.  
- Since `a ^ a = 0` and `a ^ 0 = a`, all duplicate numbers cancel each other out, leaving the single number.  
- Return the final result.

Time Complexity: O(n), where n is the number of elements in nums  
Space Complexity: O(1)
"""

class Solution:
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result
