"""
Problem: Baseball Game
LeetCode #682
Difficulty: Easy
Link: https://leetcode.com/problems/baseball-game/

Problem Statement:
You are keeping score of a baseball game with strange rules.  
The game consists of several rounds, where the scores are recorded in a list of strings `operations`.  
Each operation is one of the following:
1. An integer x — Record a new score of x.
2. "+" — Record a new score that is the sum of the previous two scores.
3. "D" — Record a new score that is double the previous score.
4. "C" — Invalidate and remove the previous score.

Return the sum of all the scores after performing all the operations.

Examples:
Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
Round 1: "5" → [5]
Round 2: "2" → [5, 2]
Round 3: "C" → remove last → [5]
Round 4: "D" → double last → [5, 10]
Round 5: "+" → sum last two → [5, 10, 15]
Total = 5 + 10 + 15 = 30

Approach:
- Use a stack to keep track of valid scores.
- Iterate through operations:
  - If it's an integer, push it to stack.
  - If "C", pop the last score.
  - If "D", push double the last score.
  - If "+", push the sum of last two scores.
- Return the sum of all elements in the stack.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def calPoints(self, operations):
        stack = []

        for op in operations:
            if op == "C":
                # Remove last valid score
                stack.pop()
            elif op == "D":
                # Double last valid score
                stack.append(2 * stack[-1])
            elif op == "+":
                # Sum of last two scores
                stack.append(stack[-1] + stack[-2])
            else:
                # Integer score
                stack.append(int(op))

        # Total sum of valid scores
        return sum(stack)
