"""
Problem: Number of Provinces
LeetCode #547
Difficulty: Medium
Link: https://leetcode.com/problems/number-of-provinces/

Problem Statement:
There are n cities. Some of them are connected, while some are not.
If city A is connected to city B, and city B is connected to city C,
then city A is connected to city C.

You are given an n x n matrix isConnected where:
- isConnected[i][j] = 1 means city i and city j are directly connected
- isConnected[i][j] = 0 means they are not connected

Return the total number of provinces.
A province is a group of directly or indirectly connected cities.

Examples:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

Approach: DFS on Adjacency Matrix
---------------------------------
- Treat each city as a node in an undirected graph.
- The matrix itself represents graph connections.
- Use DFS to visit all cities in the same province.
- Each DFS call marks one complete province.

Steps:
1. Maintain a visited array.
2. Iterate through each city:
      - If not visited, start DFS.
      - Increment province count.
3. DFS marks all reachable cities from that city.

Time Complexity:
- O(n²), because we scan the entire adjacency matrix.

Space Complexity:
- O(n), for visited array and recursion stack.
"""

class Solution(object):
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        def dfs(city):
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                provinces += 1

        return provinces
