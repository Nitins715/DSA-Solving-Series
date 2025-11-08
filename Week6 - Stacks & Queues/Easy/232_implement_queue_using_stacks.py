"""
Problem: Implement Queue using Stacks
LeetCode #232
Difficulty: Easy
Link: https://leetcode.com/problems/implement-queue-using-stacks/

Problem Statement:
Implement a first in first out (FIFO) queue using only two stacks. 
The implemented queue should support all the functions of a normal queue: push, pop, peek, and empty.

Implement the MyQueue class:
- void push(int x) — Pushes element x to the back of the queue.
- int pop() — Removes the element from the front of the queue and returns it.
- int peek() — Returns the element at the front of the queue.
- boolean empty() — Returns true if the queue is empty, false otherwise.

Notes:
- You must use only standard stack operations: push, pop, peek/top, and isEmpty.
- You may use two stacks.

Examples:
Input:
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]

Output:
[null, null, null, 1, 1, false]

Explanation:
MyQueue myQueue = new MyQueue();
myQueue.push(1);
myQueue.push(2);
myQueue.peek();  // return 1
myQueue.pop();   // return 1
myQueue.empty(); // return false

Approach:
- Use two stacks: `stack_in` for push operations and `stack_out` for pop/peek operations.
- When popping or peeking:
  - If `stack_out` is empty, move all elements from `stack_in` to `stack_out` (reverses order).
- This ensures FIFO behavior using LIFO stacks.

Time Complexity:
- Push: O(1)
- Pop/Peek (amortized): O(1)
Space Complexity: O(n)
"""

class MyQueue(object):
    def __init__(self):
        # Stack used for enqueue operations
        self.stack_in = []
        # Stack used for dequeue operations
        self.stack_out = []

    def push(self, x):
        """Push element x to the back of the queue."""
        self.stack_in.append(x)

    def pop(self):
        """Removes the element from in front of the queue and returns it."""
        self._move()
        return self.stack_out.pop()

    def peek(self):
        """Get the front element."""
        self._move()
        return self.stack_out[-1]

    def empty(self):
        """Returns whether the queue is empty."""
        return not self.stack_in and not self.stack_out

    def _move(self):
        """
        Move all elements from stack_in to stack_out if stack_out is empty.
        This ensures correct queue order (FIFO).
        """
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
