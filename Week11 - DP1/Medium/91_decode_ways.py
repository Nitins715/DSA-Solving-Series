"""
Problem: Decode Ways
LeetCode #91
Difficulty: Medium
Link: https://leetcode.com/problems/decode-ways/

Problem Statement:
A message containing letters from A-Z can be encoded into numbers using the mapping:
'A' -> "1", 'B' -> "2", ..., 'Z' -> "26".

Given a string s containing only digits, return the number of ways to decode it.

Examples:
Input: s = "12"
Output: 2
Explanation:
"12" can be decoded as:
- "AB" (1 2)
- "L" (12)

Input: s = "226"
Output: 3
Explanation:
- "BZ" (2 26)
- "VF" (22 6)
- "BBF" (2 2 6)

Input: s = "06"
Output: 0

Key Insight:
This is a **Dynamic Programming** problem.
At each position, we consider:
- One-digit decode
- Two-digit decode (if valid)

Approach: Dynamic Programming (Space Optimized)
-----------------------------------------------
Let:
- prev2 = number of ways to decode up to i-2
- prev1 = number of ways to decode up to i-1

Steps:
1. If string starts with '0' → return 0.
2. Initialize:
   - prev2 = 1 (empty string)
   - prev1 = 1 (first character)
3. Iterate from index 2 to n:
   - current = 0
   - If one-digit number is between 1 and 9 → add prev1
   - If two-digit number is between 10 and 26 → add prev2
4. Slide window forward.
5. Return prev1.

Time Complexity:
- O(n)

Space Complexity:
- O(1)
"""

class Solution(object):
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0

        prev2 = 1  # dp[0]
        prev1 = 1  # dp[1]

        for i in range(2, len(s) + 1):
            curr = 0

            # One-digit decode
            if s[i - 1] != '0':
                curr += prev1

            # Two-digit decode
            two_digit = int(s[i - 2:i])
            if 10 <= two_digit <= 26:
                curr += prev2

            prev2 = prev1
            prev1 = curr

        return prev1
