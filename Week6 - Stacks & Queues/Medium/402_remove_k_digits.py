"""
Problem: Remove K Digits
LeetCode #402
Difficulty: Medium
Link: https://leetcode.com/problems/remove-k-digits/

Problem Statement:
Given a string num representing a non-negative integer and an integer k,
remove k digits from the number so that the new number is the smallest possible.

Note:
- The result should not contain leading zeros.
- If removing all digits results in an empty string, return "0".

Examples:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove digits 4, 3, and 2 to get the smallest possible number 1219.

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 to get 0200 → "200".

Input: num = "10", k = 2
Output: "0"

Approach:
- Use a stack to build the smallest possible number.
- Iterate through digits:
  - While the top of the stack is greater than the current digit and k > 0:
    - Pop from stack (remove larger digits to make number smaller).
  - Append current digit to stack.
- If k remains > 0 after iteration, remove from the end of the stack.
- Join stack to form the result string and strip leading zeros.
- Return "0" if the result is empty after stripping zeros.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def removeKdigits(self, num, k):
        stack = []

        for digit in num:
            # Remove larger previous digits if beneficial
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        # If still need to remove digits, remove from end
        while k > 0 and stack:
            stack.pop()
            k -= 1

        # Build final result and strip leading zeros
        result = ''.join(stack).lstrip('0')

        return result if result else "0"
