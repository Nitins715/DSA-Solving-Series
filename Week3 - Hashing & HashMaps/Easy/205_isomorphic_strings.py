"""
Problem: Isomorphic Strings  
LeetCode #205  
Difficulty: Easy  
Link: https://leetcode.com/problems/isomorphic-strings/  

Problem Statement:  
Given two strings s and t, determine if they are isomorphic.  
Two strings s and t are isomorphic if the characters in s can be replaced to get t.  
All occurrences of a character must be replaced with another character  
while preserving the order of characters.  
No two characters may map to the same character,  
but a character may map to itself.

Examples:  
Input: s = "egg", t = "add"  
Output: true  

Input: s = "foo", t = "bar"  
Output: false  

Input: s = "paper", t = "title"  
Output: true  

Approach:  
- If lengths differ, return False.  
- Use two dictionaries to store mapping from s → t and t → s.  
- For each character pair (c1, c2):
  - If c1 already mapped to a different c2 → False.  
  - If c2 already mapped to a different c1 → False.  
  - Otherwise, store both mappings.  
- If loop completes, return True.

Time Complexity: O(n), where n is the length of the strings  
Space Complexity: O(n), for storing character mappings
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for c1, c2 in zip(s, t):
            if c1 in s_to_t and s_to_t[c1] != c2:
                return False
            if c2 in t_to_s and t_to_s[c2] != c1:
                return False
            s_to_t[c1] = c2
            t_to_s[c2] = c1

        return True
