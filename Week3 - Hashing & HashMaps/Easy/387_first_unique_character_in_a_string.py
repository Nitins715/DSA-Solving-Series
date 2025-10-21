"""
Problem: First Unique Character in a String  
LeetCode #387  
Difficulty: Easy  
Link: https://leetcode.com/problems/first-unique-character-in-a-string/  

Problem Statement:  
Given a string s, find the first non-repeating character in it and return its index.  
If it does not exist, return -1.

Examples:  
Input: s = "leetcode"  
Output: 0  

Input: s = "loveleetcode"  
Output: 2  

Input: s = "aabb"  
Output: -1  

Approach:  
- Initialize an empty dictionary to store the frequency of each character.  
- Iterate through the string to count occurrences.  
- Iterate again to find the first character with a count of 1 and return its index.  
- If none found, return -1.

Time Complexity: O(n), where n is the length of the string  
Space Complexity: O(1), since the alphabet size is fixed (at most 26 lowercase letters)
"""

class Solution(object):
    def firstUniqChar(self, s):
        freq = {}
        
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
                
        for i, ch in enumerate(s):
            if freq[ch] == 1:
                return i
        return -1
