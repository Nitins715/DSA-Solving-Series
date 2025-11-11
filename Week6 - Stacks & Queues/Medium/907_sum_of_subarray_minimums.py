"""
Problem: Sum of Subarray Minimums
LeetCode #907
Difficulty: Medium
Link: https://leetcode.com/problems/sum-of-subarray-minimums/

Problem Statement:
Given an array of integers arr, find the sum of min(b) for every contiguous subarray b of arr.  
Since the answer may be large, return the answer modulo 10^9 + 7.

Examples:
Input: arr = [3,1,2,4]
Output: 17
Explanation:
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1 → Sum = 17.

Input: arr = [11,81,94,43,3]
Output: 444

Approach:
- For each element, find:
  1. The distance to the previous smaller element (how far it extends to the left).
  2. The distance to the next smaller element (how far it extends to the right).
- Each element arr[i] contributes: arr[i] * left[i] * right[i] to the final sum.
- Use monotonic stacks to compute previous and next smaller elements efficiently.

Steps:
1. Traverse left-to-right to find previous smaller element distances.
2. Traverse right-to-left to find next smaller element distances.
3. Compute contribution for each element and sum them.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def sumSubarrayMins(self, arr):
        MOD = 10**9 + 7
        n = len(arr)

        # Arrays to store distances to previous and next smaller elements
        left = [0] * n
        right = [0] * n

        # Monotonic increasing stack for previous smaller elements
        stack = []
        for i in range(n):
            count = 1
            while stack and stack[-1][0] > arr[i]:
                count += stack.pop()[1]
            stack.append((arr[i], count))
            left[i] = count

        # Monotonic increasing stack for next smaller elements
        stack = []
        for i in range(n - 1, -1, -1):
            count = 1
            while stack and stack[-1][0] >= arr[i]:
                count += stack.pop()[1]
            stack.append((arr[i], count))
            right[i] = count

        # Calculate final sum
        total = 0
        for i in range(n):
            total += arr[i] * left[i] * right[i]

        return total % MOD
