"""
Problem: Contains Duplicate
LeetCode #217
Difficulty: Easy
Link: https://leetcode.com/problems/contains-duplicate/

Problem Statement:
Return True if any value appears at least twice in the array, else False.

Approach:
- Use a set to track seen elements.
- If current element is in set, return True.
- Else, add to set.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
