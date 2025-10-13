"""
Problem: Next Permutation
LeetCode #31
Difficulty: Medium
Link: https://leetcode.com/problems/next-permutation/

Problem Statement:
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation 
of numbers. If no such permutation exists, rearrange it as the lowest possible order (sorted in ascending order).

Examples:
Input: nums = [1,2,3]
Output: [1,3,2]

Approach:
- Traverse from the end to find the first decreasing element (pivot).
- Swap pivot with the smallest number greater than pivot on its right.
- Reverse the subarray after pivot.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        nums[i+1:] = reversed(nums[i+1:])
        