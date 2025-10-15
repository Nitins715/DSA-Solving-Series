"""
Problem: Reverse String
LeetCode #344
Difficulty: Easy
Link: https://leetcode.com/problems/reverse-string/

Problem Statement:
Write a function that reverses a string. The input string is given as an array of characters `s`.
You must do this by modifying the input array in-place with O(1) extra memory.

Examples:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Approach:
- Use two pointers: one starting at the beginning and one at the end of the array.
- Swap the characters at these pointers and move them towards the center until they meet.

Time Complexity: O(n), where n = length of s
Space Complexity: O(1)
"""

class Solution:
    def reverseString(self, s: list[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
