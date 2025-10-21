"""
Problem: 3Sum  
LeetCode #15  
Difficulty: Medium  
Link: https://leetcode.com/problems/3sum/  

Problem Statement:  
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]  
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.  
Notice that the solution set must not contain duplicate triplets.

Examples:  
Input: nums = [-1,0,1,2,-1,-4]  
Output: [[-1,-1,2],[-1,0,1]]  

Input: nums = [0,1,1]  
Output: []  

Input: nums = [0,0,0]  
Output: [[0,0,0]]  

Approach (Two-Pointer Technique):  
- Sort the array first to handle duplicates easily.  
- Iterate through each element 'i' as the first number.  
- Use two pointers (left and right) to find pairs that sum up to -nums[i].  
- Move pointers inward based on the sum comparison:
  - If sum < 0 → move left pointer right  
  - If sum > 0 → move right pointer left  
  - If sum == 0 → store triplet and skip duplicates  
- Skip duplicate elements for i, left, and right to avoid repeated triplets.

Time Complexity: O(n^2), where n is the number of elements in nums  
Space Complexity: O(1) (excluding the output list)
"""

class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicate 'i'

            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # skip duplicates for left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # skip duplicates for right
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result
