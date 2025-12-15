"""
Problem: Possible Bipartition
LeetCode #886
Difficulty: Medium
Link: https://leetcode.com/problems/possible-bipartition/

Problem Statement:
Given n people labeled from 1 to n and an array dislikes where
dislikes[i] = [a, b] means person a dislikes person b.

Return True if it is possible to split everyone into two groups such that:
- No pair of people who dislike each other are in the same group.

This is equivalent to checking whether the graph is **bipartite**.

Examples:
Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: True

Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: False

Approach: Graph Coloring (BFS / DFS)
-----------------------------------
- Treat each person as a node in an undirected graph.
- An edge between a and b means they must be in different groups.
- Try to color the graph using **two colors** (0 and 1).
- If a conflict occurs → not bipartite.

Algorithm:
1. Build adjacency list.
2. Maintain a color array initialized to -1 (uncolored).
3. For each unvisited node:
    - Assign a color.
    - BFS/DFS through neighbors, assigning opposite colors.
    - If a neighbor already has the same color → return False.
4. If all nodes can be colored → return True.

Why this works:
- Bipartite graphs are exactly graphs that can be colored with two colors.

Time Complexity:
- O(V + E), V = n, E = number of dislikes.

Space Complexity:
- O(V + E)
"""

from collections import defaultdict, deque

class Solution(object):
    def possibleBipartition(self, n, dislikes):
        # Build graph
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        # -1 = uncolored, 0 and 1 are two groups
        color = [-1] * (n + 1)

        # Check each connected component
        for person in range(1, n + 1):
            if color[person] == -1:
                # Start BFS coloring
                queue = deque([person])
                color[person] = 0

                while queue:
                    curr = queue.popleft()
                    for neighbor in graph[curr]:
                        if color[neighbor] == -1:
                            color[neighbor] = 1 - color[curr]
                            queue.append(neighbor)
                        elif color[neighbor] == color[curr]:
                            return False

        return True
