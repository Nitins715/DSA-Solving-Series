"""
Problem: Sort Characters By Frequency
LeetCode #451
Difficulty: Medium
Link: https://leetcode.com/problems/sort-characters-by-frequency/

Problem Statement:
Given a string s, sort it in decreasing order based on the frequency of the characters.
Return the sorted string.

Examples:
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice, while 'r' and 't' appear once.

Input: s = "cccaaa"
Output: "cccaaa"
Explanation: Both 'c' and 'a' appear three times, so either order is fine.

Input: s = "Aabb"
Output: "bbAa"
Explanation: 'b' appears twice, 'A' and 'a' appear once. Case matters.

Approach:
- Count the frequency of each character using a dictionary.
- Sort the characters by their frequency in descending order.
- Rebuild the string by repeating each character according to its frequency.

Time Complexity: O(n log n), due to sorting
Space Complexity: O(n)
"""

class Solution:
    def frequencySort(self, s: str) -> str:
        # Step 1: Count frequency of each character
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # Step 2: Sort characters by frequency (descending)
        sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # Step 3: Build the result string
        result = ""
        for ch, count in sorted_chars:
            result += ch * count

        return result
