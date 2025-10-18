"""
Problem: Decode String
LeetCode #394
Difficulty: Medium
Link: https://leetcode.com/problems/decode-string/

Problem Statement:
Given an encoded string, return its decoded version.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets 
is repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid and there are no extra spaces.

Examples:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Input: s = "3[a2[c]]"
Output: "accaccacc"

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Approach:
- Use a stack to decode the string.
- Traverse the string character by character.
- When a number is found, determine the full multiplier.
- When encountering '[', push the current string and multiplier onto the stack.
- When encountering ']', pop from the stack and combine.
- Otherwise, keep appending characters to the current string.

Time Complexity: O(n), where n = length of the string
Space Complexity: O(n), due to the stack
"""

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        current_str = ""

        for ch in s:
            if ch.isdigit():
                current_num = current_num * 10 + int(ch)
            elif ch == '[':
                stack.append((current_str, current_num))
                current_str = ""
                current_num = 0
            elif ch == ']':
                prev_str, num = stack.pop()
                current_str = prev_str + current_str * num
            else:
                current_str += ch

        return current_str
