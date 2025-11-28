"""
Problem: Sort Characters By Frequency
LeetCode #451
Difficulty: Medium
Link: https://leetcode.com/problems/sort-characters-by-frequency/

Problem Statement:
Given a string s, sort it in decreasing order based on the frequency of characters.
If two characters have the same frequency, their order does not matter.

Example:
Input: s = "tree"
Frequencies:
    t -> 1
    r -> 1
    e -> 2
Sorted: "eetr" or "eert"

Input: s = "cccaaa"
Frequencies:
    c -> 3
    a -> 3
Possible outputs: "cccaaa" or "aaaccc"

Input: s = "Aabb"
Frequencies:
    A -> 1
    a -> 1
    b -> 2
Output: "bbAa" or "bbaA"

Approach:
- Count frequency of each character using a Counter.
- Use a **max-heap** to always pick the character with highest frequency.
- Python's heapq is a min-heap, so we store (-frequency, char).
- Pop characters from the heap and build the result string.

Alternative:
- Use bucket sort where index = frequency (works well because max freq ≤ len(s)).

Time Complexity:
- O(n log k) where k = number of unique characters (at most 62 or so)
- Effectively O(n)

Space Complexity:
- O(k) for heap + O(n) for output string
"""

import heapq
from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        freq = Counter(s)
        maxheap = []

        # Build max-heap using negative frequencies
        for ch, count in freq.items():
            heapq.heappush(maxheap, (-count, ch))

        result = []

        # Pop highest-frequency characters first
        while maxheap:
            count, ch = heapq.heappop(maxheap)
            result.append(ch * (-count))

        return "".join(result)
