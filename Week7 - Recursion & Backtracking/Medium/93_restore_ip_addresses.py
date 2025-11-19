"""
Problem: Restore IP Addresses
LeetCode #93
Difficulty: Medium
Link: https://leetcode.com/problems/restore-ip-addresses/

Problem Statement:
A valid IP address consists of exactly four integers (each between 0 and 255),
separated by single dots, and cannot have leading zeros except for the number 0 itself.

Given a string s containing only digits, return all possible valid IP addresses 
that can be formed by inserting dots into s.
Return the results in any order.

Examples:
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

Input: s = "0000"
Output: ["0.0.0.0"]

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

Approach:
- Use **backtracking** to try placing dots in the string.
- At each step, choose a segment of length 1 to 3 digits.
- Check if the segment is valid:
  - It must be ≤ 255.
  - It must not have leading zeros unless it's "0".
- Stop when:
  - We form exactly 4 parts.
  - The entire string is consumed.
- When both conditions meet → append valid IP.

Time Complexity: O(3^4) → constant, since max 4 segments
Space Complexity: O(1) excluding output
"""

class Solution(object):
    def restoreIpAddresses(self, s):
        res = []

        def backtrack(i, parts):
            # If we have 4 parts and consumed all chars → valid IP
            if len(parts) == 4:
                if i == len(s):
                    res.append(".".join(parts))
                return

            # Try segments of length 1 to 3
            for length in range(1, 4):
                if i + length > len(s):
                    break

                segment = s[i:i+length]

                # Segment validity checks:
                # - No leading zeros unless "0"
                # - <= 255
                if (segment.startswith("0") and len(segment) > 1) or int(segment) > 255:
                    continue

                parts.append(segment)
                backtrack(i + length, parts)
                parts.pop()

        backtrack(0, [])
        return res
