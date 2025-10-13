"""
Problem: Find the Duplicate Number
LeetCode #287
Difficulty: Medium
Link: https://leetcode.com/problems/find-the-duplicate-number/

Problem Statement:
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), 
prove that at least one duplicate number must exist. Find the duplicate.

Examples:
Input: nums = [1,3,4,2,2]
Output: 2

Approach:
- Use Floyd's Tortoise and Hare (Cycle Detection) algorithm:
  - Treat nums as a linked list where value points to next index.
  - Find cycle entrance which is the duplicate.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def findDuplicate(self, nums):
        # Phase 1: Detect intersection point
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: Find entrance to cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow