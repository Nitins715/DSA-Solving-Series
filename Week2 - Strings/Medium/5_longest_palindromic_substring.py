"""
Problem: Longest Palindromic Substring
LeetCode #5
Difficulty: Medium
Link: https://leetcode.com/problems/longest-palindromic-substring/

Problem Statement:
Given a string s, return the longest palindromic substring in s.

Examples:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Input: s = "cbbd"
Output: "bb"

Input: s = "a"
Output: "a"

Input: s = "ac"
Output: "a"

Approach:
- Use the "Expand Around Center" technique.
- For each character (and each pair of characters for even-length palindromes), expand outward while both ends match.
- Track the start and end indices of the longest palindrome found.
- Return the substring using the recorded indices.

Time Complexity: O(n²), where n = length of s
Space Complexity: O(1)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_from_center(left: int, right: int) -> tuple[int, int]:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1  # Return the boundaries of the palindrome

        start, end = 0, 0
        for i in range(len(s)):
            # Odd-length palindrome
            l1, r1 = expand_from_center(i, i)
            # Even-length palindrome
            l2, r2 = expand_from_center(i, i + 1)

            # Choose the longer one
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]
