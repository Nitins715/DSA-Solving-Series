"""
Problem: Reorganize String
LeetCode #767
Difficulty: Medium
Link: https://leetcode.com/problems/reorganize-string/

Problem Statement:
Given a string s, rearrange the characters so that **no two adjacent characters are the same**.
Return any valid rearrangement.
If it is impossible, return "".

Examples:
Input: s = "aab"
Output: "aba"

Input: s = "aaab"
Output: ""
(because 'a' occurs 3 times, cannot separate enough)

Approach:
Use a **max-heap** to always place the character with the highest remaining frequency.

Algorithm:
1. Count frequencies using Counter.
2. Push pairs (-freq, char) into a max-heap.
3. Repeatedly:
    - Pop two most frequent characters: (count1, ch1), (count2, ch2)
    - Append them to the result one by one.
    - Decrease their counts and push back if they still have remaining frequency.
4. If only one character remains:
    - If count = 1, append it.
    - If count > 1, not possible → return "".

Why this works?
- Always placing the most frequent unused character ensures no character clusters too early.
- By choosing two characters at a time, we ensure separation.

Time Complexity:
- O(n log k), where k is number of unique characters (≤ 26)
Space Complexity:
- O(n) for result
- O(k) for heap
"""

import heapq
from collections import Counter

class Solution(object):
    def reorganizeString(self, s):
        freq = Counter(s)

        # Build a max-heap (negative frequency)
        maxheap = [(-count, ch) for ch, count in freq.items()]
        heapq.heapify(maxheap)

        result = []

        while len(maxheap) > 1:
            count1, ch1 = heapq.heappop(maxheap)
            count2, ch2 = heapq.heappop(maxheap)

            # Append the two most frequent chars
            result.append(ch1)
            result.append(ch2)

            # Decrease counts and reinsert if still remaining
            if count1 + 1 < 0:  # because stored as negative
                heapq.heappush(maxheap, (count1 + 1, ch1))
            if count2 + 1 < 0:
                heapq.heappush(maxheap, (count2 + 1, ch2))

        # If one last element remains
        if maxheap:
            count, ch = heapq.heappop(maxheap)
            if count != -1:  # more than one occurrence left → impossible
                return ""
            result.append(ch)

        return "".join(result)
