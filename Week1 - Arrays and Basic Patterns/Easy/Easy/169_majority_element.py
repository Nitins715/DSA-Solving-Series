"""
Problem: Majority Element
LeetCode #169
Difficulty: Easy
Link: https://leetcode.com/problems/majority-element/

Problem Statement:
Given an array `nums` of size n, return the majority element. 
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Examples:
Input: nums = [3,2,3]
Output: 3

Input: nums = [2,2,1,1,1,2,2]
Output: 2

Approach:
- Use the Boyer-Moore Voting Algorithm:
    - Initialize `candidate` as None and `count` as 0.
    - Traverse through the array:
        - If count is 0, set candidate to the current number.
        - Increment count if current number equals candidate; otherwise, decrement count.
- Return the candidate at the end.

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def majorityElement(self, nums):
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate