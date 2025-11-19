"""
Problem: Permutations II
LeetCode #47
Difficulty: Medium
Link: https://leetcode.com/problems/permutations-ii/

Problem Statement:
Given a collection of numbers nums that may contain duplicates,
return all possible unique permutations in any order.

Examples:
Input: nums = [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

Input: nums = [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

Approach:
- Sort nums so duplicates are adjacent.
- Use **backtracking** to generate permutations.
- Maintain a used[] array.
- At each step:
  - Skip nums[i] if:
      - It is identical to nums[i-1], AND
      - nums[i-1] has not been used in the current permutation
    (This prevents duplicate permutations.)
- Build permutations until length equals len(nums).

Time Complexity: O(n * n!)
Space Complexity: O(n)
"""

class Solution(object):
    def permuteUnique(self, nums):
        nums.sort()
        res = []
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(list(path))
                return

            for i in range(len(nums)):
                # Skip used elements
                if used[i]:
                    continue
                # Skip duplicates where previous identical element wasn't used
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False

        backtrack([])
        return res
