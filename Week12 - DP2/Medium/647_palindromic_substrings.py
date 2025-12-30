"""
Problem: Palindromic Substrings
LeetCode #647
Difficulty: Medium
Link: https://leetcode.com/problems/palindromic-substrings/

Problem Statement:
Given a string s, return the number of palindromic substrings in it.

A substring is a contiguous sequence of characters within the string.
A string is a palindrome when it reads the same backward as forward.

Single-character substrings are palindromes by definition.

Examples:
Input: s = "abc"
Output: 3
Explanation:
"a", "b", "c"

Input: s = "aaa"
Output: 6
Explanation:
"a", "a", "a", "aa", "aa", "aaa"

Key Insight:
This problem can be efficiently solved using the
**Expand Around Center** technique.

Each palindrome is defined by its center:
- One center for odd-length palindromes
- Two centers for even-length palindromes

Approach: Expand Around Center
------------------------------
Steps:
1. Initialize count = 0.
2. For each index i in the string:
   - Expand around center (i, i) → odd-length palindromes
   - Expand around center (i, i + 1) → even-length palindromes
3. For each expansion:
   - While left >= 0 and right < len(s) and s[left] == s[right]:
       increment count
       move left--, right++
4. Return count.

Time Complexity:
- O(n²)

Space Complexity:
- O(1)
"""

class Solution(object):
    def countSubstrings(self, s):
        def expandAroundCenter(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        total = 0
        for i in range(len(s)):
            # Odd-length palindromes
            total += expandAroundCenter(i, i)
            # Even-length palindromes
            total += expandAroundCenter(i, i + 1)

        return total
