"""
Problem: String to Integer (atoi)
LeetCode #8
Difficulty: Medium
Link: https://leetcode.com/problems/string-to-integer-atoi/

Problem Statement:
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

Rules:
1. Read in and ignore any leading whitespace.
2. Check if the next character (if not already at the end) is '-' or '+' to determine the sign.
3. Read in the next characters until a non-digit is encountered.
4. Convert the digits into an integer.
5. Clamp the integer to the 32-bit signed integer range:
   [-2³¹, 2³¹ - 1] = [-2147483648, 2147483647]
6. Return the integer as the final result.

Examples:
Input: s = "42"
Output: 42

Input: s = "   -42"
Output: -42

Input: s = "4193 with words"
Output: 4193

Input: s = "words and 987"
Output: 0

Input: s = "-91283472332"
Output: -2147483648

Approach:
- Trim whitespace.
- Detect sign if present.
- Iterate over characters, building the number until a non-digit is found.
- Clamp to 32-bit integer bounds if overflow occurs.

Time Complexity: O(n), where n = length of s
Space Complexity: O(1)
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        sign = 1
        i = 0
        if s[0] in ['-', '+']:
            if s[0] == '-':
                sign = -1
            i += 1

        result = 0
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        result *= sign

        # Clamp the value within the 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result
