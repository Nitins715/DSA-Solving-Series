"""
Problem: Happy Number  
LeetCode #202  
Difficulty: Easy  
Link: https://leetcode.com/problems/happy-number/  

Problem Statement:  
Write an algorithm to determine if a number n is a happy number.  
A happy number is defined by the following process:  
- Starting with any positive integer, replace the number by the sum of the squares of its digits.  
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle that does not include 1.  
- Those numbers for which this process ends in 1 are happy numbers.

Examples:  
Input: n = 19  
Output: true  
Explanation:  
1² + 9² = 82  
8² + 2² = 68  
6² + 8² = 100  
1² + 0² + 0² = 1  

Input: n = 2  
Output: false  

Approach:  
- Define a helper function to calculate the sum of squares of digits of a number.  
- Use a set to track numbers already seen to detect loops.  
- Repeat the process until the number becomes 1 (happy) or repeats (unhappy).  
- Return True if 1 is reached, else False.

Time Complexity: O(log n), as the number of digits determines the iterations  
Space Complexity: O(1) for numeric operations (O(log n) if counting visited numbers)
"""

class Solution(object):
    def isHappy(self, n):
        def get_next(num):
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total
        
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        
        return n == 1
