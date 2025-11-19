"""
Problem: Generate Parentheses
LeetCode #22
Difficulty: Medium
Link: https://leetcode.com/problems/generate-parentheses/

Problem Statement:
Given n pairs of parentheses, write a function to generate all combinations
of well-formed parentheses.

Examples:
Input: n = 3
Output:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

Input: n = 1
Output: ["()"]

Approach:
- Use **backtracking** to build valid parentheses strings.
- Maintain two counters:
  - `open_count` → number of '(' used so far
  - `close_count` → number of ')' used so far
- Rules:
  1. We can add '(' if open_count < n.
  2. We can add ')' if close_count < open_count.
- When the length of the current string equals 2*n, add it to result.

Time Complexity: O(2^n) (actually Catalan number Cn)
Space Complexity: O(n) recursion depth
"""

class Solution(object):
    def generateParenthesis(self, n):
        res = []

        def backtrack(curr, open_count, close_count):
            # Completed valid string
            if len(curr) == 2 * n:
                res.append("".join(curr))
                return

            # Add '(' if possible
            if open_count < n:
                curr.append('(')
                backtrack(curr, open_count + 1, close_count)
                curr.pop()

            # Add ')' if valid
            if close_count < open_count:
                curr.append(')')
                backtrack(curr, open_count, close_count + 1)
                curr.pop()

        backtrack([], 0, 0)
        return res
