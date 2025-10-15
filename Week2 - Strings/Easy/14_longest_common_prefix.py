"""
Problem: Longest Common Prefix  
LeetCode #14  
Difficulty: Easy  
Link: https://leetcode.com/problems/longest-common-prefix/  

Problem Statement:  
Write a function to find the longest common prefix string amongst an array of strings.  
If there is no common prefix, return an empty string "".

Examples:  
Input: strs = ["flower","flow","flight"]  
Output: "fl"  

Input: strs = ["dog","racecar","car"]  
Output: ""  

Approach:  
- If the list is empty, return "" immediately.  
- Assume the first string is the prefix.  
- Iterate through all other strings and shorten the prefix until it matches each string's beginning.  
- If the prefix becomes empty, return "" early.  
- Return the remaining prefix after checking all strings.

Time Complexity: O(n * m), where n = number of strings and m = length of the shortest string  
Space Complexity: O(1)
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
