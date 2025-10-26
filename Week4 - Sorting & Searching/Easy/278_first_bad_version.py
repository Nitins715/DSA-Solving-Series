"""
Problem: First Bad Version  
LeetCode #278  
Difficulty: Easy  
Link: https://leetcode.com/problems/first-bad-version/  

Problem Statement:  
You are a product manager and currently leading a team to develop a new product.  
Unfortunately, the latest version of your product fails the quality check.  
Since each version is developed based on the previous one,  
all the versions after a bad version are also bad.  

Suppose you have n versions [1, 2, ..., n] and you want to find out  
the first bad one, which causes all the following ones to be bad.  

You are given an API `isBadVersion(version)` which returns whether version is bad.  
Implement a function to find the first bad version.  
You should minimize the number of API calls.  

Examples:  
Input: n = 5, first_bad = 4  
Output: 4  
Explanation:  
isBadVersion(3) → False  
isBadVersion(4) → True  
So, the first bad version is 4.  

Approach (Binary Search):  
- Use binary search to minimize API calls.  
- Initialize left = 1 and right = n.  
- While left < right:
  - Find mid = (left + right) // 2.  
  - If isBadVersion(mid) is True → possible answer, move right = mid.  
  - Else → move left = mid + 1.  
- Return left (the first bad version).  

Time Complexity: O(log n)  
Space Complexity: O(1)
"""

# The isBadVersion API is already defined in the problem
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n):
        left, right = 1, n
        
        while left < right:
            mid = (left + right) // 2
            
            if isBadVersion(mid):       
                right = mid  # mid might be the first bad version
            else:
                left = mid + 1  # first bad version is after mid
        
        return left
