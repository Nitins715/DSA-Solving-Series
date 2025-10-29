"""
Problem: Median of Two Sorted Arrays  
LeetCode #4  
Difficulty: Hard  
Link: https://leetcode.com/problems/median-of-two-sorted-arrays/  

Problem Statement:  
Given two sorted arrays nums1 and nums2 of size m and n respectively,  
return the median of the two sorted arrays.  
The overall run time complexity should be O(log (m + n)).  

Example:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.0  

Optimized Approach (Binary Search Partition):  
- Perform binary search on the smaller array.
- Partition both arrays so that:
  - Left partition = first half of total elements
  - max(left1, left2) <= min(right1, right2)
- If total length is odd → median = max(left1, left2)
- If even → median = (max(left1, left2) + min(right1, right2)) / 2.0

Time Complexity: O(log(min(m, n)))  
Space Complexity: O(1)
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2

        l, r = 0, m
        while True:
            i = (l + r) // 2
            j = half - i  # ensures total elements on left = total//2

            left1 = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')
            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')

            # Partition condition
            if left1 <= right2 and left2 <= right1:
                if total % 2:
                    return float(min(right1, right2))
                return (max(left1, left2) + min(right1, right2)) / 2.0

            elif left1 > right2:
                r = i - 1
            else:
                l = i + 1
