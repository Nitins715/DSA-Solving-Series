"""
Problem: Partition Labels
LeetCode #763
Difficulty: Medium
Link: https://leetcode.com/problems/partition-labels/

Problem Statement:
You are given a string s. You need to partition the string into as many parts as possible 
so that each letter appears in at most one part, and return a list of integers representing 
the size of these parts.

Examples:
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partitions are "ababcbaca", "defegde", "hijhklij".

Input: s = "eccbbbbdec"
Output: [10]

Approach:
- Record the last index of each character in the string.
- Traverse the string while keeping track of the current partition’s end (the farthest last index seen so far).
- When the current index equals the current partition’s end, that means we can close this partition.
- Record its size and start a new partition.

Time Complexity: O(n), where n = length of s
Space Complexity: O(1), since we only store info for 26 lowercase English letters
"""

class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last_index = {ch: i for i, ch in enumerate(s)}
        result = []
        start = end = 0

        for i, ch in enumerate(s):
            end = max(end, last_index[ch])
            if i == end:
                result.append(end - start + 1)
                start = i + 1

        return result
