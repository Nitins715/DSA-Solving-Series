"""
Problem: Intersection of Two Arrays  
LeetCode #349  
Difficulty: Easy  
Link: https://leetcode.com/problems/intersection-of-two-arrays/  

Problem Statement:  
Given two integer arrays nums1 and nums2, return an array of their intersection.  
Each element in the result must be unique, and you may return the result in any order.

Examples:  
Input: nums1 = [1,2,2,1], nums2 = [2,2]  
Output: [2]  

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]  
Output: [9,4]  

Approach:  
- Initialize an empty result list.  
- For each element in nums1, check if it exists in nums2 and is not already in the result.  
- If so, add it to the result.  
- Return the result list.

Time Complexity: O(n * m), where n and m are the lengths of nums1 and nums2  
Space Complexity: O(k), where k is the number of unique intersecting elements
"""

class Solution(object):
    def intersection(self, nums1, nums2):
        result = []
        
        for num in nums1:
            if num in nums2 and num not in result:
                result.append(num)
        
        return result
