"""
Problem: Reconstruct Itinerary
LeetCode #332
Difficulty: Hard
Link: https://leetcode.com/problems/reconstruct-itinerary/

Problem Statement:
You are given a list of airline tickets where tickets[i] = [from, to].
Reconstruct the itinerary in order such that:
- You use all the tickets exactly once.
- You start from "JFK".
- If multiple valid itineraries exist, return the one with the
  **smallest lexical order**.

Example:
Input:
tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]

Input:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],
           ["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]

Approach: Hierholzer’s Algorithm (Eulerian Path)
------------------------------------------------
Key Observations:
- Each ticket is a directed edge.
- We must use **all edges exactly once** → Eulerian path problem.
- Lexical order requirement → always choose smallest destination first.

Steps:
1. Build a graph using adjacency lists.
2. Sort destinations lexicographically.
3. Use DFS:
    - While there are outgoing edges:
        - Always take the smallest available destination.
    - Append airport to result when no edges left.
4. Reverse the result to get correct itinerary.

Why this works:
- Hierholzer’s algorithm guarantees all edges are used exactly once.
- Sorting ensures lexicographically smallest itinerary.

Time Complexity:
- O(E log E), sorting edges
- DFS traversal: O(E)

Space Complexity:
- O(E), recursion stack + graph
"""

from collections import defaultdict
import heapq

class Solution(object):
    def findItinerary(self, tickets):
        graph = defaultdict(list)

        # Build graph with min-heaps for lexical order
        for src, dst in tickets:
            heapq.heappush(graph[src], dst)

        route = []

        def dfs(airport):
            while graph[airport]:
                next_airport = heapq.heappop(graph[airport])
                dfs(next_airport)
            route.append(airport)

        dfs("JFK")
        return route[::-1]
