"""
Problem: Valid Anagram
LeetCode #242
Difficulty: Easy
Link: https://leetcode.com/problems/valid-anagram/

Problem Statement:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase.

Examples:
Input: s = "anagram", t = "nagaram"
Output: True

Input: s = "rat", t = "car"
Output: False

Approach:
- First, check if both strings have the same length.
- Create a dictionary (or array) to count occurrences of each character in `s`.
- Decrease the count for each character in `t`.
- If all counts return to zero, then `t` is an anagram of `s`.

Time Complexity: O(n), where n = length of s
Space Complexity: O(1) if character set is fixed (like lowercase English letters)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        # Count characters in s
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        # Subtract counts using t
        for ch in t:
            if ch not in count:
                return False
            count[ch] -= 1
            if count[ch] < 0:
                return False

        return True
