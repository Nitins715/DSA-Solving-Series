"""
Problem: Course Schedule II
LeetCode #210
Difficulty: Medium
Link: https://leetcode.com/problems/course-schedule-ii/

Problem Statement:
You are given:
- numCourses courses labeled from 0 to numCourses - 1
- prerequisites where prerequisites[i] = [a, b] means
  you must take course b before course a

Return a valid order in which you can finish all courses.
If it is impossible, return an empty array.

Examples:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] (or [0,2,1,3])

Approach: Topological Sort (Kahn’s Algorithm – BFS)
---------------------------------------------------
- This is a **directed graph** problem.
- We need to return the topological ordering.
- If a cycle exists → return [].

Steps:
1. Build adjacency list and indegree array.
2. Push all nodes with indegree 0 into queue.
3. Pop from queue, add to result.
4. Reduce indegree of neighbors; push if indegree becomes 0.
5. If result size == numCourses → valid order.
   Else → cycle exists.

Time Complexity:
- O(V + E), V = courses, E = prerequisites

Space Complexity:
- O(V + E)
"""

from collections import defaultdict, deque

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        graph = defaultdict(list)
        indegree = [0] * numCourses

        # Build graph
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        # Queue for nodes with indegree 0
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        order = []

        # BFS Topological Sort
        while queue:
            curr = queue.popleft()
            order.append(curr)

            for neighbor in graph[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # If not all courses included → cycle
        return order if len(order) == numCourses else []
