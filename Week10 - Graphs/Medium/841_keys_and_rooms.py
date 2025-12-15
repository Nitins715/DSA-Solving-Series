"""
Problem: Keys and Rooms
LeetCode #841
Difficulty: Medium
Link: https://leetcode.com/problems/keys-and-rooms/

Problem Statement:
There are n rooms labeled from 0 to n-1.
Each room may contain keys to other rooms.

You start in room 0.
Return True if you can visit **all rooms**, otherwise False.

Examples:
Input: rooms = [[1],[2],[3],[]]
Output: True

Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: False

Approach: Graph Traversal (DFS / BFS)
-------------------------------------
- Treat each room as a node in a graph.
- A key from room i to room j is a directed edge i → j.
- Starting from room 0, perform DFS or BFS.
- Track visited rooms.
- If all rooms are visited → return True.

Time Complexity:
- O(n + k), where k = total number of keys

Space Complexity:
- O(n) for visited set / recursion stack
"""

class Solution(object):
    def canVisitAllRooms(self, rooms):
        visited = set()

        def dfs(room):
            if room in visited:
                return
            visited.add(room)

            for key in rooms[room]:
                dfs(key)

        dfs(0)
        return len(visited) == len(rooms)
