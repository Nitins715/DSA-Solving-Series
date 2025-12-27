"""
Problem: House Robber II
LeetCode #213
Difficulty: Medium
Link: https://leetcode.com/problems/house-robber-ii/

Problem Statement:
You are a professional robber planning to rob houses arranged in a circle.
Each house has a certain amount of money stashed.

Adjacent houses have security systems connected, and it will automatically
contact the police if two adjacent houses are robbed on the same night.

Because houses are arranged in a circle:
- The first house is adjacent to the last house.

Return the maximum amount of money you can rob without alerting the police.

Examples:
Input: nums = [2,3,2]
Output: 3
Explanation:
- Rob house 2 only

Input: nums = [1,2,3,1]
Output: 4
Explanation:
- Rob houses 1 and 3

Key Insight:
This is an extension of **House Robber I** with a circular constraint.

You cannot rob both:
- first house and last house together

So split into two linear subproblems:
1. Rob houses from index 0 to n-2
2. Rob houses from index 1 to n-1

Take the maximum of both.

Approach: Dynamic Programming (Two Runs)
----------------------------------------
Steps:
1. If only one house → return its value.
2. Define a helper function to solve House Robber I on a range.
3. Compute:
   - rob(nums[0 : n-1])
   - rob(nums[1 : n])
4. Return the maximum of the two results.

Time Complexity:
- O(n)

Space Complexity:
- O(1)
"""

class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses):
            prev2 = 0  # max money up to house i-2
            prev1 = 0  # max money up to house i-1

            for money in houses:
                curr = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = curr

            return prev1

        # Case 1: Exclude last house
        money1 = rob_linear(nums[:-1])
        # Case 2: Exclude first house
        money2 = rob_linear(nums[1:])

        return max(money1, money2)
