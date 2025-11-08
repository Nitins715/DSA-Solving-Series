"""
Problem: Next Greater Element II
LeetCode #503
Difficulty: Medium
Link: https://leetcode.com/problems/next-greater-element-ii/

Problem Statement:
Given a circular integer array nums (i.e., the next element of nums[n-1] is nums[0]),
return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array,
which means you can wrap around to the beginning if needed.
If it doesn’t exist, output -1 for that number.

Examples:
Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation:
- For 1 (index 0), next greater is 2.
- For 2 (index 1), no greater → -1.
- For 1 (index 2), wrap around → next greater is 2.

Input: nums = [5,4,3,2,1]
Output: [-1,5,5,5,5]

Approach:
- Use a stack to track indices whose next greater element hasn’t been found yet.
- Traverse the array twice (simulate circular nature using modulo `%`).
- For each element:
  - While stack not empty and current element > element at stack top index:
    - Pop and set next greater for that index.
  - Only push index onto stack during first pass (i < n).
- Result array initialized with -1.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [-1] * n
        stack = []  # Stack to hold indices

        # Loop twice to simulate circular array
        for i in range(2 * n):
            while stack and nums[i % n] > nums[stack[-1]]:
                index = stack.pop()
                res[index] = nums[i % n]
            if i < n:
                stack.append(i)

        return res
