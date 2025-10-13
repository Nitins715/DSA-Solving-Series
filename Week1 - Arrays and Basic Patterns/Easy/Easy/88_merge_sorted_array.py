"""
Problem: Merge Sorted Array
LeetCode #88
Difficulty: Easy
Link: https://leetcode.com/problems/merge-sorted-array/

Problem Statement:
Given two sorted arrays nums1 and nums2, merge nums2 into nums1 as one sorted array. 
nums1 has size m+n with first m elements valid; nums2 has size n.

Approach:
- Use two pointers starting from end of nums1 and nums2.
- Place larger element at the end.
- Continue until all nums2 elements merged.

Time Complexity: O(m+n)
Space Complexity: O(1)
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
