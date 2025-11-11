"""
Problem: Validate Stack Sequences
LeetCode #946
Difficulty: Medium
Link: https://leetcode.com/problems/validate-stack-sequences/

Problem Statement:
Given two integer arrays pushed and popped, each with distinct values,
return true if this could have been the result of a sequence of push and pop operations on an initially empty stack.

Examples:
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: True
Explanation: 
We might do the following sequence:
push(1), push(2), push(3), push(4), pop() → 4,
push(5), pop() → 5, pop() → 3, pop() → 2, pop() → 1.

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: False
Explanation: 1 cannot be popped before 2.

Approach:
- Use a stack to simulate the push and pop operations.
- Iterate over each element in `pushed`:
  - Push it onto the stack.
  - While the top of the stack equals the next element to pop, pop it and move to the next in `popped`.
- At the end, if all elements have been popped correctly, the stack will be empty.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def validateStackSequences(self, pushed, popped):
        stack = []
        j = 0  # Pointer for popped

        for x in pushed:
            stack.append(x)  # Simulate push
            # Keep popping while top matches popped[j]
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        # If all elements matched correctly, stack should be empty
        return not stack
