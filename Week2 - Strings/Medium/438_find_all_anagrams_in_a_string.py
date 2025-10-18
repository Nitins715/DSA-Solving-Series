"""
Problem: Find All Anagrams in a String
LeetCode #438
Difficulty: Medium
Link: https://leetcode.com/problems/find-all-anagrams-in-a-string/

Problem Statement:
Given two strings s and p, return an array of all the start indices of p's anagrams in s.
You may return the answer in any order.

Examples:
Input: s = "cbaebabacd", p = "abc"
Output: [0, 6]
Explanation: The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Input: s = "abab", p = "ab"
Output: [0, 1, 2]

Approach:
- Use the sliding window technique.
- Maintain two frequency counters: one for `p` and one for the current window in `s`.
- Slide the window across `s`, updating counts.
- If both frequency counters match, the current window is an anagram of `p`.

Time Complexity: O(n), where n = length of s
Space Complexity: O(1) (since we only store counts for 26 lowercase letters)
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []

        result = []
        s_count = [0] * 26
        p_count = [0] * 26

        for ch in p:
            p_count[ord(ch) - ord('a')] += 1

        for i in range(len(s)):
            # Add current character to the window
            s_count[ord(s[i]) - ord('a')] += 1

            # Remove character that's left the window
            if i >= len(p):
                s_count[ord(s[i - len(p)]) - ord('a')] -= 1

            # Compare window and pattern counts
            if s_count == p_count:
                result.append(i - len(p) + 1)

        return result
