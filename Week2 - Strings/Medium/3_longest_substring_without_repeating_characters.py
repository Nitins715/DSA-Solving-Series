"""
Problem: Longest Substring Without Repeating Characters
LeetCode #3
Difficulty: Medium
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Problem Statement:
Given a string s, find the length of the longest substring without repeating characters.

Examples:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.

Approach:
- Use a sliding window technique with two pointers (left and right).
- Use a set to store characters in the current window.
- Expand the window by moving the right pointer.
- If a duplicate character is found, shrink the window from the left until the duplicate is removed.
- Keep track of the maximum window size during the process.

Time Complexity: O(n), where n = length of s
Space Complexity: O(k), where k = number of unique characters in the string
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
