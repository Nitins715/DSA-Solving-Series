"""
Problem: Find if Path Exists in Graph
LeetCode #1971
Difficulty: Easy
Link: https://leetcode.com/problems/find-if-path-exists-in-graph/

Problem Statement:
You are given:
- n nodes labeled from 0 to n-1
- edges[] where each edge = [u, v]
- two nodes: source and destination

Return True if there exists **any path** between source and destination.

Example:
Input:
n = 3
edges = [[0,1],[1,2]]
source = 0, destination = 2
Output: True

Approach: DFS (or BFS) on an Undirected Graph
---------------------------------------------
1. Build adjacency list from edges.
2. Use DFS/BFS to explore neighbors.
3. Return True if we reach destination.

Since the graph is undirected, add edges both ways.

Time Complexity:
- O(n + e), where e = number of edges.

Space Complexity:
- O(n + e) for adjacency list + visited set.
"""

from collections import defaultdict, deque

class Solution(object):
    def validPath(self, n, edges, source, destination):
        if source == destination:
            return True

        # Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # BFS
        queue = deque([source])
        visited = set([source])

        while queue:
            node = queue.popleft()
            if node == destination:
                return True

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return False
