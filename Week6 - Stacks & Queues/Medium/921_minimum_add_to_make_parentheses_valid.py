"""
Problem: Minimum Add to Make Parentheses Valid
LeetCode #921
Difficulty: Medium
Link: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

Problem Statement:
A parentheses string is valid if and only if:
1. It is the empty string,
2. It can be written as AB (A concatenated with B), where A and B are valid strings, or
3. It can be written as (A), where A is a valid string.

Given a parentheses string s, return the minimum number of parentheses that must be added 
to make the resulting string valid.

Examples:
Input: s = "())"
Output: 1

Input: s = "((("
Output: 3

Input: s = "()"
Output: 0

Input: s = "()))(("
Output: 4

Approach:
- Use two counters:
  - `open_needed`: counts how many '(' are required to balance extra ')'.
  - `close_needed`: counts how many ')' are required to balance extra '('.
- Traverse each character:
  - If '(', increment `close_needed` (expecting one more ')').
  - If ')':
    - If `close_needed` > 0, it balances one '(' → decrement it.
    - Otherwise, we need an extra '(' → increment `open_needed`.
- The total additions needed = `open_needed + close_needed`.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def minAddToMakeValid(self, s):
        open_needed = 0   # Count of '(' needed
        close_needed = 0  # Count of ')' needed

        for ch in s:
            if ch == '(':
                close_needed += 1
            else:  # ch == ')'
                if close_needed > 0:
                    close_needed -= 1
                else:
                    open_needed += 1

        return open_needed + close_needed
