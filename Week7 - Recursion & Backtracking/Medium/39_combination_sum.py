"""
Problem: Combination Sum
LeetCode #39
Difficulty: Medium
Link: https://leetcode.com/problems/combination-sum/

Problem Statement:
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.

You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.

Two combinations are unique if the frequency of each number is different.

Examples:
Input: candidates = [2,3,6,7], target = 7
Output: [[7],[2,2,3]]

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Input: candidates = [2], target = 1
Output: []

Approach:
- Use **backtracking** to explore combinations.
- For each candidate, we have two options:
  1. Include it (stay at same index because reuse is allowed).
  2. Move to next candidate.
- If at any point the current sum exceeds target → stop.
- When the sum equals the target → add the current path.

Time Complexity: O(N^(T/M)), where T = target, M = smallest candidate  
Space Complexity: O(target) recursion depth
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        res = []

        def backtrack(i, curr, total):
            # If total exceeds target, stop exploring further
            if total > target:
                return

            # Found valid combination
            if total == target:
                res.append(list(curr))
                return

            # If no candidates left
            if i == len(candidates):
                return

            # Option 1: Include candidates[i]
            curr.append(candidates[i])
            backtrack(i, curr, total + candidates[i])
            curr.pop()

            # Option 2: Skip candidates[i]
            backtrack(i + 1, curr, total)

        backtrack(0, [], 0)
        return res
