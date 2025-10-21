"""
Problem: Word Pattern  
LeetCode #290  
Difficulty: Easy  
Link: https://leetcode.com/problems/word-pattern/  

Problem Statement:  
Given a pattern and a string s, find if s follows the same pattern.  
Here "follow" means a full match — each letter in pattern maps to exactly one word in s, and vice versa.

Examples:  
Input: pattern = "abba", s = "dog cat cat dog"  
Output: true  

Input: pattern = "abba", s = "dog cat cat fish"  
Output: false  

Input: pattern = "aaaa", s = "dog cat cat dog"  
Output: false  

Input: pattern = "abba", s = "dog dog dog dog"  
Output: false  

Approach:  
- Split the string s into words.  
- If lengths of pattern and words differ, return False.  
- Use two dictionaries to ensure one-to-one mapping between pattern characters and words.  
- For each pair (char, word):
  - If char is already mapped to a different word, return False.  
  - If word is already mapped to a different char, return False.  
- Return True if the full mapping is consistent.

Time Complexity: O(n), where n is the number of words in s  
Space Complexity: O(n), due to the mappings stored
"""

class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        char_to_word = {}
        word_to_char = {}
        
        for c, w in zip(pattern, words):
            if c in char_to_word and char_to_word[c] != w:
                return False
            if w in word_to_char and word_to_char[w] != c:
                return False
            char_to_word[c] = w
            word_to_char[w] = c
        
        return True
