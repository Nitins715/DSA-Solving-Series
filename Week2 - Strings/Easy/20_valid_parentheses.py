"""
Problem: Valid Parentheses  
LeetCode #20  
Difficulty: Easy  
Link: https://leetcode.com/problems/valid-parentheses/  

Problem Statement:  
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.  
An input string is valid if:  
1. Open brackets must be closed by the same type of brackets.  
2. Open brackets must be closed in the correct order.  
3. Every close bracket has a corresponding open bracket of the same type.  

Examples:  
Input: s = "()"  
Output: true  

Input: s = "()[]{}"  
Output: true  

Input: s = "(]"  
Output: false  

Approach:  
- Use a stack to keep track of opening brackets.  
- For every closing bracket, check if the top of the stack has the matching opening bracket.  
- If not, return False.  
- After processing all characters, the stack should be empty for the string to be valid.  

Time Complexity: O(n)  
Space Complexity: O(n)
"""

class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping:
                top = stack.pop() if stack else '#'
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)
        return not stack
