"""
Problem: Two Sum
LeetCode #1
Difficulty: Easy
Link: https://leetcode.com/problems/two-sum/

Problem Statement:
Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.

Examples:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Approach:
- Use a hashmap (dictionary) to store numbers and their indices.
- For each number, compute complement = target - num.
- If complement exists in map, return indices.
- Ensures O(n) time and O(n) space.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def twoSum(self, nums, target):
        mapping = {}
        for index, val in enumerate(nums):
            diff = target - val
            if diff in mapping:
                return [mapping[diff], index]
            mapping[val] = index
