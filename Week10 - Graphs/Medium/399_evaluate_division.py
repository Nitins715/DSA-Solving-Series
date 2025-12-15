"""
Problem: Evaluate Division
LeetCode #399
Difficulty: Medium
Link: https://leetcode.com/problems/evaluate-division/

Problem Statement:
You are given equations in the form:
    A / B = value
and some queries:
    C / D = ?

Return the answers to all queries.
If the answer cannot be determined, return -1.0.

Examples:
Input:
equations = [["a","b"],["b","c"]]
values = [2.0, 3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

Output:
[6.0, 0.5, -1.0, 1.0, -1.0]

Approach: Graph + DFS
---------------------
- Treat each variable as a node in a graph.
- Each equation A / B = k creates:
      A → B with weight k
      B → A with weight 1/k
- For each query, perform DFS to find a path from numerator to denominator.
- Multiply edge weights along the path.

Key Observations:
- If either variable is missing → answer = -1.0
- If numerator == denominator and variable exists → answer = 1.0

Time Complexity:
- Building graph: O(E)
- Each query DFS: O(V + E) worst case

Space Complexity:
- O(V + E)
"""

from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
        # Build graph
        graph = defaultdict(list)

        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1.0 / val))

        def dfs(curr, target, visited, product):
            if curr == target:
                return product

            visited.add(curr)

            for neighbor, weight in graph[curr]:
                if neighbor not in visited:
                    res = dfs(neighbor, target, visited, product * weight)
                    if res != -1.0:
                        return res

            return -1.0

        results = []

        for num, den in queries:
            if num not in graph or den not in graph:
                results.append(-1.0)
            elif num == den:
                results.append(1.0)
            else:
                results.append(dfs(num, den, set(), 1.0))

        return results
