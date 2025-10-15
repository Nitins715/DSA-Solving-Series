"""
Problem: Find the Index of the First Occurrence in a String
LeetCode #28
Difficulty: Easy
Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Problem Statement:
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

Examples:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0

Input: haystack = "leetcode", needle = "leeto"
Output: -1

Approach:
- Iterate through each possible starting index in haystack.
- For each index, check if the substring of haystack matches the needle.
- If a match is found, return the starting index.
- If no match exists, return -1.

Time Complexity: O(n * m), where
    n = length of haystack
    m = length of needle
Space Complexity: O(1)
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)

        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i

        return -1
