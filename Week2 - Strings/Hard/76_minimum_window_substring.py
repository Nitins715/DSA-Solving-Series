"""
Problem: Minimum Window Substring
LeetCode #76
Difficulty: Hard
Link: https://leetcode.com/problems/minimum-window-substring/

Problem Statement:
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s 
such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".

Examples:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Input: s = "a", t = "a"
Output: "a"

Input: s = "a", t = "aa"
Output: ""

Approach:
- Use the sliding window technique.
- Maintain two frequency maps: one for `t` (required characters) and one for the current window.
- Expand the right pointer to include characters until all characters from `t` are satisfied.
- Then move the left pointer to minimize the window while still satisfying the condition.
- Track the smallest valid window found during the traversal.

Time Complexity: O(n + m), where
    n = length of s
    m = length of t
Space Complexity: O(k), where k = number of unique characters in t
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        # Step 1: Count required characters
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        have = {}
        have_count = 0
        need_count = len(need)
        res = [float('inf'), 0, 0]  # [window_length, left, right]
        left = 0

        # Step 2: Expand right pointer
        for right, ch in enumerate(s):
            have[ch] = have.get(ch, 0) + 1
            if ch in need and have[ch] == need[ch]:
                have_count += 1

            # Step 3: Contract from the left if all chars are satisfied
            while have_count == need_count:
                if (right - left + 1) < res[0]:
                    res = [right - left + 1, left, right]

                have[s[left]] -= 1
                if s[left] in need and have[s[left]] < need[s[left]]:
                    have_count -= 1
                left += 1

        # Step 4: Return the smallest window
        return "" if res[0] == float('inf') else s[res[1]:res[2] + 1]
