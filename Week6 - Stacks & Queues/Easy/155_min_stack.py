"""
Problem: Min Stack
LeetCode #155
Difficulty: Medium
Link: https://leetcode.com/problems/min-stack/

Problem Statement:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
- void push(int val) — Pushes the element val onto the stack.
- void pop() — Removes the element on the top of the stack.
- int top() — Gets the top element.
- int getMin() — Retrieves the minimum element in the stack.

Examples:
Input:
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output:
[null,null,null,null,-3,null,0,-2]

Explanation:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

Approach:
- Use two stacks:
  1. `stack` to store all elements.
  2. `min_stack` to store the minimum value at each level of the stack.
- On push:
  - Push val to `stack`.
  - Push min(val, top of min_stack) to `min_stack`.
- On pop:
  - Pop from both stacks.
- `getMin` always returns top of `min_stack`.

This ensures constant time for all operations.

Time Complexity:
- Push: O(1)
- Pop: O(1)
- Top: O(1)
- GetMin: O(1)

Space Complexity: O(n)
"""

class MinStack(object):
    def __init__(self):
        # Stack to hold all values
        self.stack = []
        # Stack to hold the minimum value at each level
        self.min_stack = []

    def push(self, val):
        """Push element val onto stack."""
        self.stack.append(val)
        # Push the minimum value up to this point
        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)

    def pop(self):
        """Removes the element on top of the stack."""
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        """Get the top element."""
        return self.stack[-1]

    def getMin(self):
        """Retrieve the minimum element in the stack."""
        return self.min_stack[-1]
