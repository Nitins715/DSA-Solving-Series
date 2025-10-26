"""
Problem: Valid Perfect Square  
LeetCode #367  
Difficulty: Easy  
Link: https://leetcode.com/problems/valid-perfect-square/  

Problem Statement:  
Given a positive integer num, return true if num is a perfect square or false otherwise.  
A perfect square is an integer that is the square of an integer.  
You must not use any built-in library function, such as sqrt().  

Examples:  
Input: num = 16  
Output: True  

Input: num = 14  
Output: False  

Approach (Binary Search):  
- Use binary search between 1 and num // 2 to check if a mid * mid equals num.  
- If mid * mid == num → return True.  
- If mid * mid < num → move left to mid + 1.  
- Else → move right to mid - 1.  
- If no perfect square found, return False.  

Time Complexity: O(log n)  
Space Complexity: O(1)
"""

class Solution:
    def isPerfectSquare(self, num):
        if num < 2:
            return True
        
        left, right = 1, num // 2
        
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            
            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
