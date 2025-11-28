"""
Problem: Task Scheduler
LeetCode #621
Difficulty: Medium
Link: https://leetcode.com/problems/task-scheduler/

Problem Statement:
You are given:
- A list of tasks (uppercase letters A–Z)
- A non-negative integer n (cooldown time)

Each task takes 1 unit of time.  
Identical tasks must be at least n units apart.

Return the **minimum total time** needed to finish all tasks.

Example:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Optimal order:
A _ _ A _ _ A
B _ _ B _ _ B
Total time = 8

Explanation:
We place the most frequent task and fill gaps with other tasks or idle slots.

Another Example:
Input: tasks = ["A","A","A","B","B","B"], n = 0
No cooldown needed → simply length of tasks.
Output: 6

Approach (Greedy + Math Formula):
Let:
- max_freq = highest frequency of any task
- count_max = number of tasks appearing max_freq times

Formula:
Minimum time =
    max( len(tasks),  (max_freq - 1) * (n + 1) + count_max )

Why?
- (max_freq - 1) blocks, each block has size (n + 1)
- Add the last block containing all max-frequency tasks

Example:
tasks = ["A","A","A","B","B","B"], n = 2

max_freq = 3 (A and B)
count_max = 2

Time = (3 - 1) * (2 + 1) + 2 = 8

Time Complexity:
- O(n) to count frequencies

Space Complexity:
- O(1) (only 26 tasks max)
"""

from collections import Counter

class Solution(object):
    def leastInterval(self, tasks, n):
        freq = Counter(tasks)
        max_freq = max(freq.values())
        count_max = list(freq.values()).count(max_freq)

        # Apply formula
        part_count = max_freq - 1
        part_length = n + 1
        empty_slots = part_count * part_length + count_max

        return max(len(tasks), empty_slots)
