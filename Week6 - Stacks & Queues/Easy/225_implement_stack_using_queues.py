"""
Problem: Implement Stack using Queues
LeetCode #225
Difficulty: Easy
Link: https://leetcode.com/problems/implement-stack-using-queues/

Problem Statement:
Implement a last-in-first-out (LIFO) stack using only two queues. 
The implemented stack should support all the functions of a normal stack: push, pop, top, and empty.

Implement the MyStack class:
- void push(int x) — Pushes element x onto the stack.
- int pop() — Removes the element on the top of the stack and returns it.
- int top() — Returns the element on the top of the stack.
- boolean empty() — Returns true if the stack is empty, false otherwise.

Examples:
Input:
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]

Output:
[null, null, null, 2, 2, false]

Explanation:
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top();   // return 2
myStack.pop();   // return 2
myStack.empty(); // return false

Approach:
- Use two queues (queue1 and queue2) to simulate stack behavior.
- Push operation:
  - Push element to queue2.
  - Move all elements from queue1 to queue2 (so newest is always at the front).
  - Swap queue1 and queue2.
- Pop and top operations are then O(1), since top element is at front of queue1.

Time Complexity:
- Push: O(n)
- Pop: O(1)
- Top: O(1)
Space Complexity: O(n)
"""

from collections import deque

class MyStack(object):
    def __init__(self):
        # Initialize two queues
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x):
        """Push element x onto stack."""
        # Add new element to queue2
        self.queue2.append(x)

        # Move all elements from queue1 to queue2
        while self.queue1:
            self.queue2.append(self.queue1.popleft())

        # Swap queues so queue1 always has the current stack order
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        """Removes the element on top of the stack and returns it."""
        return self.queue1.popleft()

    def top(self):
        """Get the top element."""
        return self.queue1[0]

    def empty(self):
        """Returns whether the stack is empty."""
        return not self.queue1
