"""
Problem: Subarray Sum Equals K
LeetCode #560
Difficulty: Medium
Link: https://leetcode.com/problems/subarray-sum-equals-k/

Problem Statement:
Given an integer array nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Examples:
Input: nums = [1,1,1], k = 2
Output: 2

Approach:
- Use prefix sum with a hashmap to store frequency of sums.
- For each element, check if (current_sum - k) exists in the hashmap and increment count.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def subarraySum(self, nums, k):
        from collections import defaultdict
        count = 0
        cum_sum = 0
        prefix = defaultdict(int)
        prefix[0] = 1

        for num in nums:
            cum_sum += num
            count += prefix.get(cum_sum - k, 0)
            prefix[cum_sum] += 1

        return count
