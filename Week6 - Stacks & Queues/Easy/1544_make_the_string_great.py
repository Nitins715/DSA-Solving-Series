"""
Problem: Make The String Great
LeetCode #1544
Difficulty: Easy
Link: https://leetcode.com/problems/make-the-string-great/

Problem Statement:
Given a string s of lowercase and uppercase English letters,
a good string is a string that doesn't have two adjacent characters s[i] and s[i + 1]
where:
- s[i] is a lowercase letter and s[i + 1] is the same letter but uppercase, or
- s[i] is an uppercase letter and s[i + 1] is the same letter but lowercase.

Return the string after making it good.
The answer is guaranteed to be unique.

Examples:
Input: s = "leEeetcode"
Output: "leetcode"
Explanation: Remove "Ee" → "leetcode"

Input: s = "abBAcC"
Output: ""
Explanation: Remove "abBAcC" → "" (empty string)

Input: s = "s"
Output: "s"

Approach:
- Use a stack to build the "good" string.
- Iterate through each character:
  - If the stack is not empty and the current char is the same letter as the top of the stack
    but in opposite case (difference in ASCII value = 32), pop the top.
  - Else, push the character onto the stack.
- Join the stack to form the final good string.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def makeGood(self, s):
        stack = []

        for char in s:
            # Check if last char and current char form a bad pair (same letter, opposite case)
            if stack and abs(ord(stack[-1]) - ord(char)) == 32:
                stack.pop()
            else:
                stack.append(char)

        # Join remaining characters to form the final string
        return "".join(stack)
