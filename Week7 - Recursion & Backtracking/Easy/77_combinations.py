"""
Problem: Combinations
LeetCode #77
Difficulty: Medium
Link: https://leetcode.com/problems/combinations/

Problem Statement:
Given two integers n and k, return all possible combinations of k numbers 
chosen from the range [1, n].

You may return the answer in any order.

Examples:
Input: n = 4, k = 2
Output:
[
 [1,2],
 [1,3],
 [1,4],
 [2,3],
 [2,4],
 [3,4]
]

Input: n = 1, k = 1
Output: [[1]]

Approach:
- Use **backtracking** to build all combinations.
- Start from 1 and recursively add numbers while ensuring increasing order.
- Stop recursion when the current combination reaches size k.

Optimization:
- Use pruning: if remaining numbers are less than required to fill combination, stop early.

Time Complexity: O(C(n, k)) → number of combinations
Space Complexity: O(k) recursion depth + output storage
"""

class Solution(object):
    def combine(self, n, k):
        res = []

        def backtrack(start, path):
            # If combination is complete, add to results
            if len(path) == k:
                res.append(list(path))
                return

            # Try each possible next number
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

        backtrack(1, [])
        return res
