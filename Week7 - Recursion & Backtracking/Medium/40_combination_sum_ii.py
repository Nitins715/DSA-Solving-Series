"""
Problem: Combination Sum II
LeetCode #40
Difficulty: Medium
Link: https://leetcode.com/problems/combination-sum-ii/

Problem Statement:
Given a collection of candidate numbers (candidates) that may contain duplicates 
and a target number (target), return all unique combinations in candidates 
where the candidate numbers sum to target.

Each number in candidates may be used **at most once**.
The solution set must not contain duplicate combinations.

Examples:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
 [1,1,6],
 [1,2,5],
 [1,7],
 [2,6]
]

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
 [1,2,2],
 [5]
]

Approach:
- Sort the array to make it easier to skip duplicates.
- Use **backtracking**, but unlike Combination Sum (I), 
  each index can only be used once.
- While iterating at the same depth, skip candidates[i] 
  if it is the same as the previous (duplicate combination prevention).
- If total > target → stop exploring.
- If total == target → add path to result.

Time Complexity: O(2^n)
Space Complexity: O(n)
"""

class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []

        def backtrack(start, curr, total):
            if total == target:
                res.append(list(curr))
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                # Skip duplicates at the same decision level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                curr.append(candidates[i])
                backtrack(i + 1, curr, total + candidates[i])
                curr.pop()

        backtrack(0, [], 0)
        return res
