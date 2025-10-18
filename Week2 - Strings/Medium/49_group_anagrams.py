"""
Problem: Group Anagrams
LeetCode #49
Difficulty: Medium
Link: https://leetcode.com/problems/group-anagrams/

Problem Statement:
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

Examples:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]

Input: strs = ["a"]
Output: [["a"]]

Approach:
- For each word, sort its characters — the sorted word becomes a key that represents its anagram group.
- Store words with the same sorted key in a dictionary.
- Return the grouped values as a list.

Time Complexity: O(n * k log k), where  
    n = number of strings  
    k = average length of each string  
Space Complexity: O(n * k)
"""

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = {}

        for word in strs:
            key = ''.join(sorted(word))  # Sorted word acts as the unique key
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(word)

        return list(anagrams.values())
