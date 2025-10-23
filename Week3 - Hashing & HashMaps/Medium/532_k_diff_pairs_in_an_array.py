"""
Problem: K-diff Pairs in an Array  
LeetCode #532  
Difficulty: Medium  
Link: https://leetcode.com/problems/k-diff-pairs-in-an-array/  

Problem Statement:  
Given an integer array nums and an integer k,  
return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]),  
where 0 <= i < j < len(nums) and |nums[i] - nums[j]| == k.

Examples:  
Input: nums = [3,1,4,1,5], k = 2  
Output: 2  
Explanation: The pairs are (1,3) and (3,5).

Input: nums = [1,2,3,4,5], k = 1  
Output: 4  

Input: nums = [1,3,1,5,4], k = 0  
Output: 1  

Approach:  
- If k < 0, return 0 (no valid pairs).  
- For k = 0 → count numbers appearing more than once.  
- For k > 0 → use a set to check for elements that have a complement (num + k).  
- Use sets to avoid duplicate counting.  

Time Complexity: O(n)  
Space Complexity: O(n)
"""

class Solution:
    def findPairs(self, nums, k):
        if k < 0:
            return 0

        seen = set()
        pairs = set()

        for num in nums:
            if num - k in seen:
                pairs.add(num - k)
            if num + k in seen:
                pairs.add(num)
            seen.add(num)

        if k == 0:
            freq = {}
            count = 0
            for num in nums:
                if num in freq:
                    freq[num] += 1
                else:
                    freq[num] = 1
            for key in freq:
                if freq[key] > 1:
                    count += 1
            return count

        return len(pairs)
