"""
Problem: Find K-th Smallest Pair Distance  
LeetCode #719  
Difficulty: Hard  
Link: https://leetcode.com/problems/find-k-th-smallest-pair-distance/  

Problem Statement:  
The distance of a pair (a, b) is defined as the absolute difference between a and b.  

Given an integer array nums and an integer k,  
return the k-th smallest distance among all the pairs (nums[i], nums[j]) where i < j.  

Examples:  
Input: nums = [1,3,1], k = 1  
Output: 0  
Explanation: The pair distances are [0,2,2]. The 1st smallest distance is 0.  

Input: nums = [1,1,1], k = 2  
Output: 0  

Input: nums = [1,6,1], k = 3  
Output: 5  

Approach (Binary Search + Two Pointers):  
- Sort nums first.  
- The smallest possible distance = 0, and the largest = max(nums) - min(nums).  
- Use binary search on this distance range:  
  - For each mid (distance guess), count how many pairs have distance <= mid.  
  - If count >= k, move right = mid (we need smaller distances).  
  - Else, move left = mid + 1.  
- The first distance where count >= k is the k-th smallest distance.  

Counting Pairs (Two Pointer method):  
- For each right pointer, move left pointer until nums[right] - nums[left] <= mid.  
- The number of valid pairs for this right is (right - left).  

Time Complexity: O(n log W) where W = max_distance  
Space Complexity: O(1)
"""

class Solution:
    def smallestDistancePair(self, nums, k):
        nums.sort()

        def count_pairs(max_dist):
            count = 0
            left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > max_dist:
                    left += 1
                count += right - left
            return count

        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if count_pairs(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left
