"""
Problem: Find All Duplicates in an Array  
LeetCode #442  
Difficulty: Medium  
Link: https://leetcode.com/problems/find-all-duplicates-in-an-array/  

Problem Statement:  
Given an integer array nums of length n where all the integers are in the range [1, n],  
each integer appears once or twice.  
Return an array of all the integers that appear twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

Examples:  
Input: nums = [4,3,2,7,8,2,3,1]  
Output: [2,3]  

Input: nums = [1,1,2]  
Output: [1]  

Approach (In-Place Marking):  
- Iterate through each number in nums.  
- For each number, use its absolute value to find its correct index (`index = abs(num) - 1`).  
- If the number at that index is negative, it means the index has been visited before → duplicate found.  
- Otherwise, mark it as visited by multiplying by -1.  
- Return all numbers found as duplicates.

Time Complexity: O(n)  
Space Complexity: O(1)
"""

class Solution:
    def findDuplicates(self, nums):
        res = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                res.append(abs(num))
            else:
                nums[index] = -nums[index]
        return res
