"""
Problem: Word Ladder
LeetCode #127
Difficulty: Hard
Link: https://leetcode.com/problems/word-ladder/

Problem Statement:
Given two words:
- beginWord
- endWord
and a word list wordList,

Return the **length of the shortest transformation sequence** from beginWord to endWord.

Rules:
- Only one letter can be changed at a time.
- Each transformed word must exist in wordList.
- beginWord does NOT need to be in wordList.
- If no such transformation exists, return 0.

Example:
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5
Explanation:
hit → hot → dot → dog → cog

Approach: BFS with Pattern Mapping
----------------------------------
This is a shortest-path problem in an unweighted graph.

Key Idea:
- Treat each word as a node.
- Two words are connected if they differ by exactly one letter.
- Preprocess wordList to create intermediate patterns.

Example:
"hot" → "*ot", "h*t", "ho*"

Steps:
1. Build a dictionary mapping patterns → words.
2. BFS from beginWord.
3. For each word, generate all patterns.
4. Use the pattern map to find neighbors efficiently.
5. Track visited words to avoid cycles.

Why BFS?
- Each transformation has equal cost (1).
- BFS guarantees shortest path.

Time Complexity:
- O(N × L²), where N = number of words, L = word length

Space Complexity:
- O(N × L)
"""

from collections import defaultdict, deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0

        L = len(beginWord)

        # Step 1: Build pattern map
        pattern_map = defaultdict(list)
        for word in wordList:
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                pattern_map[pattern].append(word)

        # Step 2: BFS
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        while queue:
            word, level = queue.popleft()

            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]

                for next_word in pattern_map[pattern]:
                    if next_word == endWord:
                        return level + 1

                    if next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, level + 1))

                # Clear list to prevent reprocessing
                pattern_map[pattern] = []

        return 0
