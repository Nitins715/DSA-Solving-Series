"""
Problem: Asteroid Collision
LeetCode #735
Difficulty: Medium
Link: https://leetcode.com/problems/asteroid-collision/

Problem Statement:
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction:
- Positive → moving right
- Negative → moving left

Each asteroid moves at the same speed.
When two asteroids meet, the smaller one explodes.
If both are the same size, both explode.
Asteroids moving in the same direction will never meet.

Return the state of the asteroids after all collisions.

Examples:
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: 10 and -5 collide → -5 explodes.

Input: asteroids = [8,-8]
Output: []
Explanation: Both explode.

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: 2 and -5 collide → -5 explodes, then 10 and -5 collide → -5 explodes again.

Approach:
- Use a stack to simulate the asteroid collisions.
- Iterate through asteroids:
  - If current asteroid is moving right (positive), push it to the stack.
  - If moving left (negative):
    - While stack top is moving right and smaller than the current left-moving asteroid → pop (they explode).
    - If top asteroid is equal in size → both explode (pop top and skip current).
    - If top is larger → current asteroid explodes (do not push it).
    - Otherwise, push current asteroid.
- Return the stack as final state.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []

        for ast in asteroids:
            # Check for possible collisions only when ast < 0 and stack top > 0
            while stack and ast < 0 < stack[-1]:
                if stack[-1] < -ast:
                    # Stack top asteroid explodes
                    stack.pop()
                    continue
                elif stack[-1] == -ast:
                    # Both explode
                    stack.pop()
                break
            else:
                # No collision, push asteroid
                stack.append(ast)

        return stack
