"""
Problem: Sliding Window Maximum
LeetCode #239
Difficulty: Hard
Link: https://leetcode.com/problems/sliding-window-maximum/

Problem Statement:
Given an array nums and an integer k, return the max value in each sliding window of size k.

Examples:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

Approach:
- Use a deque to store indices of useful elements for current window.
- Remove indices out of window and smaller elements from deque front/back.
- The front of deque contains the max for the window.

Time Complexity: O(n)
Space Complexity: O(k)
"""

from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if not nums or k == 0:
            return []
        dq = deque()
        res = []

        for i in range(len(nums)):
            while dq and dq[0] < i - k + 1:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res
