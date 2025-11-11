"""
Problem: Decode String
LeetCode #394
Difficulty: Medium
Link: https://leetcode.com/problems/decode-string/

Problem Statement:
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets
is repeated exactly k times. You may assume that the input string is always valid and 
contains no extra spaces.

Examples:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Input: s = "3[a2[c]]"
Output: "accaccacc"

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Approach:
- Use a stack to handle nested patterns.
- Traverse each character:
  - When encountering a digit, build the full number (for multi-digit multipliers).
  - When encountering '[', push the current string and count to stack, then reset current string.
  - When encountering ']', pop from stack — repeat the substring and append to previous context.
  - When encountering a character, add it to current string.
- The final decoded string is in the `current_string`.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def decodeString(self, s):
        stack = []  # To store (previous_string, repeat_count)
        current_string = ""
        current_num = 0

        for char in s:
            if char.isdigit():
                # Build multi-digit number
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Push current context to stack
                stack.append((current_string, current_num))
                # Reset for new context
                current_string = ""
                current_num = 0
            elif char == ']':
                # Pop from stack and build the new string
                prev_string, num = stack.pop()
                current_string = prev_string + current_string * num
            else:
                # Append normal characters
                current_string += char

        return current_string
