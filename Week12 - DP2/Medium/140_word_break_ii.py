"""
Problem: Word Break II
LeetCode #140
Difficulty: Hard
Link: https://leetcode.com/problems/word-break-ii/

Problem Statement:
Given a string s and a dictionary of strings wordDict,
add spaces in s to construct all possible sentences where each word
is a valid dictionary word.

Return all such possible sentences in any order.

Each word in the dictionary may be reused multiple times.

Examples:
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]

Input: s = "pineapplepenapple",
       wordDict = ["apple","pen","applepen","pine","pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]

Key Insight:
This problem is a combination of **Dynamic Programming + DFS (Backtracking)**.

- DP is used to quickly check which prefixes can lead to valid solutions.
- DFS with memoization is used to construct all valid sentences efficiently.

Approach: DFS + Memoization
---------------------------
Steps:
1. Convert wordDict to a set for O(1) lookups.
2. Use DFS(start) to return all valid sentences that can be built from s[start:].
3. Memoize results for each start index to avoid recomputation.
4. For each possible end index:
   - If s[start:end] is a valid word,
     recursively build sentences from end.
5. Combine current word with results from recursion.
6. Return memo[0] as the final answer.

Time Complexity:
- Exponential in worst case (number of valid sentences),
  but optimized heavily using memoization.

Space Complexity:
- O(n²) for recursion stack + memo storage
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        word_set = set(wordDict)
        memo = {}

        def dfs(start):
            if start in memo:
                return memo[start]

            results = []

            if start == len(s):
                return [""]

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    sub_sentences = dfs(end)
                    for sub in sub_sentences:
                        if sub:
                            results.append(word + " " + sub)
                        else:
                            results.append(word)

            memo[start] = results
            return results

        return dfs(0)
