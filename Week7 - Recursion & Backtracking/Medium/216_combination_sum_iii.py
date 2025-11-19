"""
Problem: Combination Sum III
LeetCode #216
Difficulty: Medium
Link: https://leetcode.com/problems/combination-sum-iii/

Problem Statement:
Find all valid combinations of k numbers that sum up to n such that:
- Only numbers 1 through 9 can be used.
- Each number may be used at most once.

Return the list of all possible combinations.

Examples:
Input: k = 3, n = 7
Output: [[1,2,4]]

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]

Approach:
- Use **backtracking** to choose numbers from 1 to 9.
- Each number can be used once → increase the start index each time.
- Stop early (prune) when:
  - Current combination exceeds k length.
  - The sum exceeds n.
- When length == k and sum == n → valid combination.

Time Complexity: O(C(9, k))
Space Complexity: O(k)
"""

class Solution(object):
    def combinationSum3(self, k, n):
        res = []

        def backtrack(start, curr, total):
            if len(curr) == k:
                if total == n:
                    res.append(list(curr))
                return

            for num in range(start, 10):
                if total + num > n:
                    break
                curr.append(num)
                backtrack(num + 1, curr, total + num)
                curr.pop()

        backtrack(1, [], 0)
        return res
