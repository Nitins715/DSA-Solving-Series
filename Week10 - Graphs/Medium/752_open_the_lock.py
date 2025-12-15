"""
Problem: Open the Lock
LeetCode #752
Difficulty: Medium
Link: https://leetcode.com/problems/open-the-lock/

Problem Statement:
You have a lock with 4 circular wheels.
Each wheel has digits from 0 to 9 and can rotate forward or backward.

You are given:
- deadends: a list of blocked combinations
- target: the target combination

You start from "0000".
Return the **minimum number of moves** to reach the target.
If it is impossible, return -1.

Rules:
- You cannot enter any deadend state.
- Each move rotates one wheel by one digit (up or down).

Examples:
Input:
deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6

Input:
deadends = ["8888"], target = "0009"
Output: 1

Approach: BFS (Shortest Path in State Space)
--------------------------------------------
- Each lock combination is a node.
- Each move generates up to 8 neighbors (4 wheels × 2 directions).
- Since each move has equal cost, BFS guarantees the shortest path.

Algorithm:
1. Put all deadends into a set.
2. If "0000" is a deadend → return -1.
3. Start BFS from "0000".
4. For each state:
     - Generate all valid next states.
     - Skip visited or deadend states.
5. Stop when target is reached.

Time Complexity:
- O(10⁴), maximum states = 10000

Space Complexity:
- O(10⁴), queue + visited set.
"""

from collections import deque

class Solution(object):
    def openLock(self, deadends, target):
        dead = set(deadends)
        start = "0000"

        if start in dead:
            return -1
        if start == target:
            return 0

        queue = deque([(start, 0)])
        visited = set([start])

        while queue:
            state, steps = queue.popleft()

            if state == target:
                return steps

            for i in range(4):
                digit = int(state[i])

                for move in (-1, 1):
                    new_digit = (digit + move) % 10
                    next_state = state[:i] + str(new_digit) + state[i+1:]

                    if next_state not in dead and next_state not in visited:
                        visited.add(next_state)
                        queue.append((next_state, steps + 1))

        return -1
