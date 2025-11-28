"""
Problem: Top K Frequent Words
LeetCode #692
Difficulty: Medium
Link: https://leetcode.com/problems/top-k-frequent-words/

Problem Statement:
Given an array of strings words and an integer k:
Return the k most frequent words.

Rules:
- Sort by **frequency** (higher first).
- If two words have the same frequency, sort them **lexicographically** (alphabetically) in ascending order.

Example:
Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Frequencies:
  i -> 2
  love -> 2
  leetcode -> 1
  coding -> 1
Sorted:
  ["i", "love"] (same freq, lexicographically sorted)
Output: ["i", "love"]

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"],
       k = 4
Frequencies:
  the -> 4
  is -> 3
  sunny -> 2
  day -> 1
Output: ["the","is","sunny","day"]

Approach:
- Use a hash map (Counter) to count frequencies.
- Use a **min-heap** of size k.
- Heap ordering:
    (frequency, -lexicographic order)
  BUT Python heap is min-heap, and we want:
    - Higher frequency first → store negative frequency.
    - Lexicographically smaller word first → store word normally.

Thus push: (-freq, word)

- Pop k items from heap.
- Sort final results based on required rule (heap ensures correct priority).

Time Complexity:
- Counting: O(n)
- Heap operations: O(n log k)
- Sorting results: O(k log k)

Space Complexity:
- O(n) for frequency map.
- O(k) for heap.
"""

import heapq
from collections import Counter

class Solution(object):
    def topKFrequent(self, words, k):
        freq = Counter(words)

        heap = []
        for word, count in freq.items():
            # Push using negative count for max-heap behavior
            heapq.heappush(heap, (-count, word))

        result = []
        for _ in range(k):
            count, word = heapq.heappop(heap)
            result.append(word)

        return result
