"""
Problem: Course Schedule
LeetCode #207
Difficulty: Medium
Link: https://leetcode.com/problems/course-schedule/

Problem Statement:
There are numCourses courses labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [a, b]
means you must take course b before course a.

Return True if you can finish all courses, otherwise return False.

This problem reduces to detecting a **cycle in a directed graph**.
If there is a cycle → courses cannot be completed.

Examples:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: True

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: False (cycle exists)

Approach: Topological Sort (Kahn’s Algorithm – BFS)
---------------------------------------------------
Key idea:
- Courses form a directed graph.
- If we can topologically sort all nodes → no cycle exists.

Steps:
1. Build adjacency list and indegree array.
2. Push all nodes with indegree 0 into queue.
3. Repeatedly:
    - Remove node from queue
    - Reduce indegree of its neighbors
    - If neighbor indegree becomes 0 → add to queue
4. Count processed nodes.
5. If processed count == numCourses → return True, else False.

Time Complexity:
- O(V + E), where V = courses, E = prerequisites

Space Complexity:
- O(V + E)
"""

from collections import defaultdict, deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        indegree = [0] * numCourses

        # Build graph
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        # Queue for courses with no prerequisites
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        completed = 0

        # BFS Topological Sort
        while queue:
            node = queue.popleft()
            completed += 1

            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return completed == numCourses
