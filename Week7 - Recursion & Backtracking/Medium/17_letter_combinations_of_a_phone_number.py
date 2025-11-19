"""
Problem: Letter Combinations of a Phone Number
LeetCode #17
Difficulty: Medium
Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Problem Statement:
Given a string containing digits from 2-9, return all possible letter combinations 
that the number could represent. Return the answer in any order.

The mapping is the same as on a phone keypad:
2 → abc
3 → def
4 → ghi
5 → jkl
6 → mno
7 → pqrs
8 → tuv
9 → wxyz

Examples:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Input: digits = ""
Output: []

Input: digits = "2"
Output: ["a","b","c"]

Approach:
- Use backtracking to generate all possible combinations.
- Maintain a mapping from digit to corresponding letters.
- For each digit, append each possible letter and recurse.
- Stop when current combination length equals digits length.

Edge Case:
- If digits is empty, return [].

Time Complexity: O(3^n * 4^m)
(where n digits map to 3 letters, m digits map to 4 letters)
Space Complexity: O(n) recursion depth
"""

class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []

        mapping = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        res = []

        def backtrack(i, path):
            if i == len(digits):
                res.append("".join(path))
                return

            for ch in mapping[digits[i]]:
                path.append(ch)
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res
