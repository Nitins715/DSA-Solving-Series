"""
Problem: Relative Ranks
LeetCode #506
Difficulty: Easy
Link: https://leetcode.com/problems/relative-ranks/

Problem Statement:
You are given an integer array score of size n, where score[i] is the score of the ith athlete.
You must assign ranks to all athletes based on their scores.

Rules:
- Highest score → "Gold Medal"
- Second highest → "Silver Medal"
- Third highest → "Bronze Medal"
- All others → Rank number as a string (e.g., "4", "5", ...)

Return an array answer where answer[i] is the rank of the ith athlete.

Example:
Input: score = [5,4,3,2,1]
Sorted: [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]

Input: score = [10,3,8,9,4]
Sorted: [10,9,8,4,3]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]

Approach:
- We need to rank scores in descending order.
- Keep track of original indices so we can fill the result correctly.
- Steps:
  1. Pair each score with its index → (score, index)
  2. Sort by score descending.
  3. Assign:
       - 1st → "Gold Medal"
       - 2nd → "Silver Medal"
       - 3rd → "Bronze Medal"
       - Others → string(rank)
  4. Place results back according to original index.

Time Complexity:
- Sorting: O(n log n)
- Assigning ranks: O(n)
Overall: O(n log n)

Space Complexity:
- O(n) for result array and list of pairs.
"""

class Solution(object):
    def findRelativeRanks(self, score):
        n = len(score)
        result = [""] * n

        # Pair scores with original indices
        arr = [(s, i) for i, s in enumerate(score)]

        # Sort by score descending
        arr.sort(reverse=True)

        for rank, (s, idx) in enumerate(arr):
            if rank == 0:
                result[idx] = "Gold Medal"
            elif rank == 1:
                result[idx] = "Silver Medal"
            elif rank == 2:
                result[idx] = "Bronze Medal"
            else:
                result[idx] = str(rank + 1)

        return result
