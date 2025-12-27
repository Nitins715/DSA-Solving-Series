# File Name: 198_house_robber.py

"""
Problem: House Robber
LeetCode #198
Difficulty: Medium
Link: https://leetcode.com/problems/house-robber/

Problem Statement:
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed.

The only constraint stopping you from robbing each of them is that
adjacent houses have security systems connected, and it will automatically
contact the police if two adjacent houses are robbed on the same night.

Given an integer array nums representing the amount of money in each house,
return the maximum amount of money you can rob tonight without alerting the police.

Examples:
Input: nums = [1,2,3,1]
Output: 4
Explanation:
- Rob house 1 (1) and house 3 (3)

Input: nums = [2,7,9,3,1]
Output: 12
Explanation:
- Rob house 2 (7) and house 4 (3) and house 5 (1)

Key Insight:
This is a **Dynamic Programming** problem.
At each house, you have two choices:
- Rob the current house → skip the previous one
- Skip the current house → take the previous result

Approach: Dynamic Programming (Space Optimized)
-----------------------------------------------
Let:
- prev2 = max money robbed up to house i-2
- prev1 = max money robbed up to house i-1

For each house i:
- current = max(prev1, prev2 + nums[i])

Steps:
1. Initialize prev2 = 0, prev1 = 0
2. Iterate through each house:
   - Compute the best choice at current house
   - Slide the window forward
3. Return prev1 as the final answer

Time Complexity:
- O(n)

Space Complexity:
- O(1)
"""

class Solution(object):
    def rob(self, nums):
        prev2 = 0  # max money up to house i-2
        prev1 = 0  # max money up to house i-1

        for money in nums:
            curr = max(prev1, prev2 + money)
            prev2 = prev1
            prev1 = curr

        return prev1
