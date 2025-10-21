"""
Problem: Contains Duplicate II  
LeetCode #219  
Difficulty: Easy  
Link: https://leetcode.com/problems/contains-duplicate-ii/  

Problem Statement:  
Given an integer array nums and an integer k,  
return true if there are two distinct indices i and j in the array  
such that nums[i] == nums[j] and abs(i - j) <= k.  
Otherwise, return false.

Examples:  
Input: nums = [1,2,3,1], k = 3  
Output: true  

Input: nums = [1,0,1,1], k = 1  
Output: true  

Input: nums = [1,2,3,1,2,3], k = 2  
Output: false  

Approach:  
- Use a dictionary to store each number's latest index.  
- Iterate through the list:
  - If the number is already in the dictionary and the difference between indices ≤ k, return True.  
  - Otherwise, update the index in the dictionary.  
- If no such pair exists, return False.

Time Complexity: O(n), where n is the number of elements in nums  
Space Complexity: O(n), for storing indices in the dictionary
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        index_map = {}
        
        for i in range(len(nums)):
            num = nums[i]
            if num in index_map and i - index_map[num] <= k:
                return True
            index_map[num] = i
        
        return False
