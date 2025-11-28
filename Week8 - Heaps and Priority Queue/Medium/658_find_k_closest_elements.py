"""
Problem: Find K Closest Elements
LeetCode #658
Difficulty: Medium
Link: https://leetcode.com/problems/find-k-closest-elements/

Problem Statement:
Given a sorted integer array arr, two integers k and x:
Return the k closest integers to x in the array.

Rules:
- The result should be sorted in ascending order.
- If two numbers are equally close to x:
      Choose the smaller one.

Example:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Closest: [1,2,3,4]

Input: arr = [1,2,3,4,5], k = 4, x = -1
Closest: [1,2,3,4]

Approach:
Use **Binary Search + Two Pointers Window Shrinking**:
- Since arr is sorted, we binary search for the best starting index of a window of size k.
- Window can start between 0 and len(arr)-k.
- Compare:
      x - arr[mid]     vs     arr[mid+k] - x
  If left side is larger → shift right (mid is too far left)
  Else → shift left (mid is good or too far right)

Why this works:
- We want a window of size k with minimal total distance to x.
- Only O(log(n - k)) search, not scanning whole array.

Time Complexity:
- O(log(n - k) + k)

Space Complexity:
- O(1) (excluding output)
"""

class Solution(object):
    def findClosestElements(self, arr, k, x):
        left = 0
        right = len(arr) - k   # possible starting points

        while left < right:
            mid = (left + right) // 2

            # Compare distances:
            # If mid's element is farther from x, move right
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        # left is the start of the best window
        return arr[left:left + k]
