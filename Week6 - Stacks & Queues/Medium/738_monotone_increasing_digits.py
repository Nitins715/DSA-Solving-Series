"""
Problem: Monotone Increasing Digits
LeetCode #738
Difficulty: Medium
Link: https://leetcode.com/problems/monotone-increasing-digits/

Problem Statement:
Given an integer n, return the largest number that is less than or equal to n
and has digits in a monotone increasing order.

A number has monotone increasing digits if every pair of adjacent digits x and y
satisfy x <= y.

Examples:
Input: n = 10
Output: 9

Input: n = 1234
Output: 1234

Input: n = 332
Output: 299

Approach:
- Convert the number to a list of digits for easy manipulation.
- Traverse digits from right to left:
  - If a digit is greater than the next one, decrement it by 1 and mark the position.
  - All digits to the right of that position should be set to 9 (to maximize the result).
- Finally, convert digits back to an integer and return it.

Time Complexity: O(d), where d is the number of digits.
Space Complexity: O(d)
"""

class Solution(object):
    def monotoneIncreasingDigits(self, n):
        digits = list(str(n))
        marker = len(digits)

        # Traverse from right to left
        for i in range(len(digits) - 1, 0, -1):
            if digits[i - 1] > digits[i]:
                digits[i - 1] = str(int(digits[i - 1]) - 1)
                marker = i

        # Set all digits after marker to '9'
        for i in range(marker, len(digits)):
            digits[i] = '9'

        return int(''.join(digits))
