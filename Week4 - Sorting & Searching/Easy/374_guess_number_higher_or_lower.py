"""
Problem: Guess Number Higher or Lower  
LeetCode #374  
Difficulty: Easy  
Link: https://leetcode.com/problems/guess-number-higher-or-lower/  

Problem Statement:  
We are playing the Guess Game. The game is as follows:  
I pick a number from 1 to n. You have to guess which number I picked.  

Every time you guess wrong, the API `guess(int num)` will tell you whether  
the number I picked is higher or lower than your guess:  
-1 → My number is lower  
1  → My number is higher  
0  → Correct guess  

Implement a function to guess the number picked using the `guess` API.  

Examples:  
Input: n = 10, pick = 6  
Output: 6  

Approach (Binary Search):  
- Initialize left = 1, right = n.  
- Use binary search to minimize API calls:
  - mid = (left + right) // 2  
  - If guess(mid) == 0 → return mid  
  - If guess(mid) == -1 → the number is lower → right = mid - 1  
  - If guess(mid) == 1 → the number is higher → left = mid + 1  
- Return left when found.  

Time Complexity: O(log n)  
Space Complexity: O(1)
"""

# The guess API is already defined in the problem
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n):
        left, right = 1, n
        
        while left <= right:
            mid = (left + right) // 2
            res = guess(mid)
            
            if res == 0:
                return mid
            elif res < 0:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1
