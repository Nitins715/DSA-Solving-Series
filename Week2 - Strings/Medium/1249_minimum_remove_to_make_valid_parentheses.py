"""
Problem: Minimum Remove to Make Valid Parentheses
LeetCode #1249
Difficulty: Medium
Link: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

Problem Statement:
Given a string s of '(' , ')' and lowercase English characters,
remove the minimum number of parentheses so that the resulting string is valid.

Return any valid string.

A string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Examples:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"

Input: s = "a)b(c)d"
Output: "ab(c)d"

Input: s = "))(("
Output: ""

Approach:
- Use a stack to keep track of indices of unmatched '('.
- Traverse the string:
  - Push index for '(' onto the stack.
  - Pop when a matching ')' is found.
  - Mark invalid ')' for removal if unmatched.
- After traversal, remove remaining '(' indices left in the stack.
- Build the valid string by skipping invalid indices.

Time Complexity: O(n), where n = length of s
Space Complexity: O(n)
"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = set()
        open_stack = []

        # Step 1: Identify invalid parentheses
        for i, ch in enumerate(s):
            if ch == '(':
                open_stack.append(i)
            elif ch == ')':
                if open_stack:
                    open_stack.pop()
                else:
                    stack.add(i)

        # Step 2: Add remaining unmatched '(' indices
        stack = stack.union(set(open_stack))

        # Step 3: Build result skipping invalid indices
        result = []
        for i, ch in enumerate(s):
            if i not in stack:
                result.append(ch)

        return "".join(result)
