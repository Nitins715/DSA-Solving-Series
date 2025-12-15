"""
Problem: Clone Graph
LeetCode #133
Difficulty: Medium
Link: https://leetcode.com/problems/clone-graph/

Problem Statement:
Given a reference to a node in a **connected undirected graph**,
return a deep copy (clone) of the graph.

Each node contains:
- val: integer value
- neighbors: list of neighboring nodes

The graph may contain cycles.

Example:
Input: adjacency list = [[2,4],[1,3],[2,4],[1,3]]
Output: cloned graph with same structure and values

Approach: DFS with Hash Map (Visited Dictionary)
------------------------------------------------
Key challenge:
- Avoid infinite loops due to cycles.
- Ensure each node is cloned exactly once.

Solution:
- Use a hashmap (dictionary) to map:
      original_node → cloned_node
- Perform DFS:
    1. If node already cloned → return clone.
    2. Create a new node.
    3. Recursively clone neighbors.
    4. Attach cloned neighbors to the new node.

This guarantees:
- Correct structure
- No duplicate nodes
- Proper handling of cycles

Time Complexity:
- O(V + E), V = number of nodes, E = number of edges

Space Complexity:
- O(V), hashmap + recursion stack
"""

# Definition for a Node.
# class Node(object):
#     def __init__(self, val=0, neighbors=None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None

        visited = {}

        def dfs(curr):
            # If already cloned, return it
            if curr in visited:
                return visited[curr]

            # Clone current node
            clone = Node(curr.val)
            visited[curr] = clone

            # Clone neighbors
            for neighbor in curr.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)
