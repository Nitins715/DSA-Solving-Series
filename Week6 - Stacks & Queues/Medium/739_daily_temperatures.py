"""
Problem: Daily Temperatures
LeetCode #739
Difficulty: Medium
Link: https://leetcode.com/problems/daily-temperatures/

Problem Statement:
Given an array of integers temperatures representing the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait
after the ith day to get a warmer temperature. If there is no future day for which this is possible,
keep answer[i] == 0 instead.

Examples:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Explanation:
- Day 0 → 73 → wait 1 day to reach 74
- Day 1 → 74 → wait 1 day to reach 75
- Day 2 → 75 → wait 4 days to reach 76
- Day 3 → 71 → wait 2 days to reach 72
- Day 4 → 69 → wait 1 day to reach 72
- Day 5 → 72 → wait 1 day to reach 76
- Day 6 → 76 → no warmer → 0
- Day 7 → 73 → no warmer → 0

Approach:
- Use a stack to store indices of days whose warmer temperature hasn’t been found yet.
- Traverse through temperatures:
  - While the current temperature > temperature at top index of stack:
    - Pop index from stack, calculate difference in days, and update result.
  - Push the current index onto the stack.
- This is a **monotonic decreasing stack** pattern.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        answer = [0] * n
        stack = []  # Stack to hold indices

        for i in range(n):
            # Check if current temperature is warmer than previous days
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            stack.append(i)

        return answer
