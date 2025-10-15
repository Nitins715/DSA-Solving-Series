"""
Problem: Ransom Note
LeetCode #383
Difficulty: Easy
Link: https://leetcode.com/problems/ransom-note/

Problem Statement:
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using 
the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Examples:
Input: ransomNote = "a", magazine = "b"
Output: False

Input: ransomNote = "aa", magazine = "ab"
Output: False

Input: ransomNote = "aa", magazine = "aab"
Output: True

Approach:
- Count the frequency of each character in magazine.
- For each character in ransomNote, check if it's available in magazine.
- If a character is missing or insufficient, return False.
- Otherwise, return True.

Time Complexity: O(n + m), where
    n = length of ransomNote
    m = length of magazine
Space Complexity: O(1) (assuming only lowercase English letters)
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}

        # Count characters in magazine
        for ch in magazine:
            count[ch] = count.get(ch, 0) + 1

        # Check if ransomNote can be constructed
        for ch in ransomNote:
            if ch not in count or count[ch] == 0:
                return False
            count[ch] -= 1

        return True
