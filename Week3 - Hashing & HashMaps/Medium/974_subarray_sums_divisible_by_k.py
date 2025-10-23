"""
Problem: Subarray Sums Divisible by K  
LeetCode #974  
Difficulty: Medium  
Link: https://leetcode.com/problems/subarray-sums-divisible-by-k/  

Problem Statement:  
Given an integer array nums and an integer k,  
return the number of (contiguous) subarrays that have a sum divisible by k.

Examples:  
Input: nums = [4,5,0,-2,-3,1], k = 5  
Output: 7  
Explanation: There are 7 subarrays with sums divisible by 5.

Input: nums = [5], k = 9  
Output: 0  

Approach (Prefix Sum + Remainder Counting):  
- Use a dictionary to count the frequency of prefix sum remainders (mod k).  
- Initialize with remainder 0 having count 1 (for subarrays starting at index 0).  
- For each number, add it to the prefix sum and compute `remainder = prefix_sum % k`.  
- Adjust remainder if negative by adding k.  
- If this remainder has been seen before, it means previous subarrays had the same remainder,  
  so the subarray between them has a sum divisible by k.  
- Add that frequency to the result count.  
- Update the remainder count.  
- Return total count.

Time Complexity: O(n)  
Space Complexity: O(k)
"""

class Solution:
    def subarraysDivByK(self, nums, k):
        remainder_count = {0: 1}
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k

            # handle negative remainders
            if remainder < 0:
                remainder += k

            if remainder in remainder_count:
                count += remainder_count[remainder]
                remainder_count[remainder] += 1
            else:
                remainder_count[remainder] = 1

        return count
