"""
Problem: Intersection of Two Arrays II
LeetCode #350
Difficulty: Easy
Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/

Problem Statement:
Return the intersection of two arrays including duplicate counts.

Approach:
- Count elements of nums1 in a hashmap.
- For nums2, if element exists in map with positive count, add to result and decrement.

Time Complexity: O(n+m)
Space Complexity: O(n)
"""

class Solution(object):
    def intersect(self, nums1, nums2):
        counts = {}
        result = []
        for num in nums1:
            counts[num] = counts.get(num, 0) + 1
        for num in nums2:
            if counts.get(num, 0) > 0:
                result.append(num)
                counts[num] -= 1
        return result