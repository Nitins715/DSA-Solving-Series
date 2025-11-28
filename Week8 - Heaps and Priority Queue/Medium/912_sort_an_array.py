"""
Problem: Sort an Array
LeetCode #912
Difficulty: Medium
Link: https://leetcode.com/problems/sort-an-array/

Problem Statement:
Given an integer array nums, sort the array in ascending order and return it.
You must implement an O(n log n) sorting algorithm (not just call Python's sort).

Example:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]

Approach:
Use **Merge Sort**:
- Time complexity: O(n log n)
- Space complexity: O(n)
- Stable and guaranteed performance

Why Merge Sort?
- Works well with recursion
- Required complexity fits constraints
- Avoids worst-case O(n²) seen in naive QuickSort implementations

Merge Sort Steps:
1. Divide array into two halves.
2. Recursively sort each half.
3. Merge the two sorted halves by comparing smallest elements.

Time Complexity:
- O(n log n)

Space Complexity:
- O(n) for temporary arrays during merging
"""

class Solution(object):
    def sortArray(self, nums):

        def merge(left, right):
            result = []
            i = j = 0

            # Merge two sorted lists
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            # Append remaining elements
            result.extend(left[i:])
            result.extend(right[j:])

            return result

        def mergeSort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])

            return merge(left, right)

        return mergeSort(nums)
