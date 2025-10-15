"""
Problem: Valid Palindrome  
LeetCode #125  
Difficulty: Easy  
Link: https://leetcode.com/problems/valid-palindrome/  

Problem Statement:  
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,  
it reads the same forward and backward.  
Given a string s, return true if it is a palindrome, or false otherwise.

Examples:  
Input: s = "A man, a plan, a canal: Panama"  
Output: true  

Input: s = "race a car"  
Output: false  

Input: s = " "  
Output: true  

Approach:  
- Convert the string to lowercase.  
- Use two pointers (left and right) to compare characters from both ends.  
- Skip non-alphanumeric characters using `str.isalnum()`.  
- If characters mismatch at any point, return False.  
- If the entire string is traversed without mismatches, return True.

Time Complexity: O(n)  
Space Complexity: O(1)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
