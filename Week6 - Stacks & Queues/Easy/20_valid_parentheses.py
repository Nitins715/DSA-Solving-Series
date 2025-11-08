"""
Problem: Valid Parentheses
LeetCode #20
Difficulty: Easy
Link: https://leetcode.com/problems/valid-parentheses/

Problem Statement:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Examples:
Input: s = "()"
Output: True

Input: s = "()[]{}"
Output: True

Input: s = "(]"
Output: False

Approach:
- Use a stack to keep track of opening brackets.
- For every closing bracket, check if it matches the top of the stack.
- If mismatched or stack is empty when a closing bracket appears → return False.
- If stack is empty at the end → valid, else invalid.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def isValid(self, s):
        # Dictionary to map closing brackets to their corresponding opening brackets
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []  # Stack to hold opening brackets

        # Iterate through each character in the string
        for char in s:
            if char in mapping:
                # Pop the top element from the stack if it's not empty
                top_element = stack.pop() if stack else '#'
                # If mapping doesn't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push to stack
                stack.append(char)

        # Stack should be empty if all brackets are matched
        return not stack
