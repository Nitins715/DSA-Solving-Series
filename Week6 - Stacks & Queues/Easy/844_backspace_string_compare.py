"""
Problem: Backspace String Compare
LeetCode #844
Difficulty: Easy
Link: https://leetcode.com/problems/backspace-string-compare/

Problem Statement:
Given two strings s and t, return true if they are equal when both are typed into empty text editors.
'#' means a backspace character.

Note: After backspacing an empty text, the text remains empty.

Examples:
Input: s = "ab#c", t = "ad#c"
Output: True
Explanation: Both s and t become "ac".

Input: s = "ab##", t = "c#d#"
Output: True
Explanation: Both s and t become "".

Input: s = "a#c", t = "b"
Output: False
Explanation: s becomes "c" while t becomes "b".

Approach:
- Use a stack to simulate typing for each string.
- For each character:
  - If it's a letter, push it to the stack.
  - If it's '#', pop from the stack if not empty.
- After processing both strings, compare the final stacks.
- Alternate approach: use two pointers from end to start (optimized for space).

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def backspaceCompare(self, s, t):
        def build(string):
            stack = []
            for char in string:
                if char == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return stack

        return build(s) == build(t)
