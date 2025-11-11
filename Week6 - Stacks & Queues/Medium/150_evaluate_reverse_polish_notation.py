"""
Problem: Evaluate Reverse Polish Notation
LeetCode #150
Difficulty: Medium
Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/

Problem Statement:
You are given an array of strings tokens that represents an arithmetic expression in Reverse Polish Notation (RPN).

Evaluate the expression and return an integer that represents the value of the expression.

Valid operators are '+', '-', '*', and '/'. 
Each operand may be an integer or another expression.

Note:
- Division between two integers should truncate toward zero.
- The given RPN expression is always valid, meaning the expression always evaluates to a result, 
  and there will not be any division by zero.

Examples:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22

Approach:
- Use a stack to evaluate the postfix expression.
- For each token:
  - If it’s a number, push it to the stack.
  - If it’s an operator, pop two numbers, perform the operation, and push the result back.
- At the end, the stack will contain one element — the final result.
- Be careful with division truncation toward zero (use int(a / b)).

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            if token not in "+-*/":
                # Push numbers to the stack
                stack.append(int(token))
            else:
                # Pop the top two operands
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    # Division should truncate toward zero
                    stack.append(int(a / b))

        # Final result on top of stack
        return stack[0]
