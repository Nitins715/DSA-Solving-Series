"""
Problem: Russian Doll Envelopes
LeetCode #354
Difficulty: Hard
Link: https://leetcode.com/problems/russian-doll-envelopes/

Problem Statement:
You are given a list of envelopes, where each envelope is represented
as [width, height].

One envelope can fit into another if and only if both the width and height
of one envelope are strictly greater than the width and height of the other.

Return the maximum number of envelopes you can Russian doll
(i.e., put one inside another).

Examples:
Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation:
The maximum number of envelopes you can nest is:
[2,3] → [5,4] → [6,7]

Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1

Key Insight:
This problem reduces to a **Longest Increasing Subsequence (LIS)** problem
after sorting the envelopes correctly.

Critical Sorting Rule:
- Sort by width in ascending order
- If widths are equal, sort by height in descending order

This prevents invalid nesting when widths are the same.

Approach: LIS with Binary Search (O(n log n))
---------------------------------------------
Steps:
1. Sort envelopes using the rule above.
2. Extract the heights from the sorted envelopes.
3. Find the LIS on heights using patience sorting / binary search.
4. The length of the LIS is the answer.

Time Complexity:
- O(n log n)

Space Complexity:
- O(n)
"""

import bisect

class Solution(object):
    def maxEnvelopes(self, envelopes):
        if not envelopes:
            return 0

        # Sort by width asc, height desc
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # Extract heights
        heights = [h for _, h in envelopes]

        # LIS on heights
        lis = []
        for h in heights:
            idx = bisect.bisect_left(lis, h)
            if idx == len(lis):
                lis.append(h)
            else:
                lis[idx] = h

        return len(lis)
