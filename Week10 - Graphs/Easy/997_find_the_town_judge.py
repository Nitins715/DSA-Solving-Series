"""
Problem: Find the Town Judge
LeetCode #997
Difficulty: Easy
Link: https://leetcode.com/problems/find-the-town-judge/

Problem Statement:
In a town, there are n people labeled from 1 to n.

Rules:
1. The town judge trusts nobody.
2. Everybody (except the judge) trusts the judge.
3. There is exactly one judge, or none.

You are given an array trust where trust[i] = [a, b]
meaning person a trusts person b.

Return the label of the town judge if one exists, otherwise return -1.

Examples:
Input: n = 2, trust = [[1,2]]
Output: 2

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

Approach: Trust Score (In-degree & Out-degree)
----------------------------------------------
Key observation:
- Judge has:
    in-degree = n - 1 (everyone trusts them)
    out-degree = 0 (trusts nobody)

We can track this using a score array:
- For each trust [a, b]:
      score[a] -= 1   (a trusts someone)
      score[b] += 1   (b is trusted)

At the end:
- The person with score == n - 1 is the judge.

Time Complexity:
- O(n + t), where t = number of trust relationships

Space Complexity:
- O(n)
"""

class Solution(object):
    def findJudge(self, n, trust):
        # Special case: only one person and no trust
        if n == 1 and not trust:
            return 1

        score = [0] * (n + 1)

        for a, b in trust:
            score[a] -= 1
            score[b] += 1

        for person in range(1, n + 1):
            if score[person] == n - 1:
                return person

        return -1
