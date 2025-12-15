"""
Problem: Network Delay Time
LeetCode #743
Difficulty: Medium
Link: https://leetcode.com/problems/network-delay-time/

Problem Statement:
You are given:
- n nodes labeled from 1 to n
- times[i] = [u, v, w] meaning it takes w time for a signal to travel from u → v
- A starting node k

Return the time it takes for all nodes to receive the signal.
If it is impossible for all nodes to receive the signal, return -1.

This is a **single-source shortest path** problem on a directed weighted graph.

Examples:
Input:
times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Approach: Dijkstra’s Algorithm (Min-Heap)
-----------------------------------------
Since all edge weights are positive:
- Dijkstra’s algorithm guarantees shortest paths.

Steps:
1. Build adjacency list from times.
2. Use a min-heap storing (current_time, node).
3. Track shortest known time to each node.
4. Always process the node with the smallest current time.
5. Update neighbors if a shorter path is found.

Final Answer:
- If all nodes are reached → return the maximum shortest time.
- Else → return -1.

Time Complexity:
- O(E log V), where E = edges, V = nodes

Space Complexity:
- O(V + E)
"""

import heapq
from collections import defaultdict

class Solution(object):
    def networkDelayTime(self, times, n, k):
        # Build adjacency list
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # Min-heap: (time, node)
        heap = [(0, k)]
        dist = {}

        while heap:
            time, node = heapq.heappop(heap)

            # If already visited with shortest time, skip
            if node in dist:
                continue

            dist[node] = time

            for nei, w in graph[node]:
                if nei not in dist:
                    heapq.heappush(heap, (time + w, nei))

        # If not all nodes reached
        if len(dist) != n:
            return -1

        # Maximum time among all shortest paths
        return max(dist.values())
