"""
Problem: Remove All Adjacent Duplicates in String II
LeetCode #1209
Difficulty: Medium
Link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

Problem Statement:
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent 
and equal letters from s and removing them, causing the left and the right side of the deleted 
substring to concatenate together.

We repeatedly make k duplicate removals until no more can be done.
Return the final string after all such duplicate removals have been made.

Examples:
Input: s = "abcd", k = 2
Output: "abcd"

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation:
First remove "eee" and "ccc", get "ddbbbdaa".
Then remove "bbb", get "dddaa".
Finally remove "ddd", get "aa".

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"

Approach:
- Use a stack to store pairs of (character, count).
- Traverse the string:
  - If the current character is the same as the one on top of the stack, increment its count.
  - If the count equals k, pop it from the stack (removing duplicates).
  - Otherwise, push a new pair onto the stack.
- Finally, rebuild the string using the stack contents.

Time Complexity: O(n), where n = length of s
Space Complexity: O(n)
"""

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # Each element is [char, count]

        for ch in s:
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()  # Remove the k duplicates
            else:
                stack.append([ch, 1])

        # Reconstruct final string
        result = ""
        for ch, count in stack:
            result += ch * count

        return result
