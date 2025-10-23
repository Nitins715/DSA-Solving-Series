"""
Problem: Longest Consecutive Sequence  
LeetCode #128  
Difficulty: Medium  
Link: https://leetcode.com/problems/longest-consecutive-sequence/  

Problem Statement:  
Given an unsorted array of integers nums,  
return the length of the longest consecutive elements sequence.  
You must write an algorithm that runs in O(n) time.

Examples:  
Input: nums = [100,4,200,1,3,2]  
Output: 4  
Explanation: The longest consecutive sequence is [1,2,3,4].  

Input: nums = [0,3,7,2,5,8,4,6,0,1]  
Output: 9  

Approach:  
- Convert the list into a set for O(1) lookups.  
- Iterate through each number and check if it is the start of a sequence  
  (i.e., num - 1 not in set).  
- If it is, keep counting forward while consecutive numbers exist.  
- Track and update the longest length found.  
- Return the maximum length after iterating through all numbers.

Time Complexity: O(n), since each number is visited once on average  
Space Complexity: O(n), for storing numbers in a set
"""

class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        num_set = set(nums)
        longest = 0

        for num in num_set:
            # start of a sequence
            if num - 1 not in num_set:
                current = num
                length = 1

                while current + 1 in num_set:
                    current += 1
                    length += 1

                if length > longest:
                    longest = length

        return longest
