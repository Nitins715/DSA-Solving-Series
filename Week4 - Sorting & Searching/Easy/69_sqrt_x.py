"""
Problem: Sqrt(x)  
LeetCode #69  
Difficulty: Easy  
Link: https://leetcode.com/problems/sqrtx/  

Problem Statement:  
Given a non-negative integer x, return the square root of x rounded down  
to the nearest integer. The returned integer should be non-negative as well.  

You must not use any built-in exponent function or operator (such as pow(x, 0.5)).  

Examples:  
Input: x = 4  
Output: 2  

Input: x = 8  
Output: 2  
Explanation: The square root of 8 is 2.828..., and since we round down, we return 2.  

Approach (Binary Search):  
- If x is 0 or 1, return x directly.  
- Use binary search between 1 and x // 2 to find the integer square root.  
- For each mid:
  - If mid * mid == x → return mid.  
  - If mid * mid < x → move left to mid + 1.  
  - Else → move right to mid - 1.  
- Return `right` (the floor value of the sqrt) after the loop ends.  

Time Complexity: O(log x)  
Space Complexity: O(1)
"""

class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        
        left, right = 1, x // 2
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            
            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right
