"""
Problem: Find K Closest Elements  
LeetCode #658  
Difficulty: Medium  
Link: https://leetcode.com/problems/find-k-closest-elements/  

Problem Statement:  
Given a sorted integer array arr, two integers k and x,  
return the k closest integers to x in the array.  

The result should also be sorted in ascending order.  
If there is a tie, the smaller elements are always preferred.  

Examples:  
Input: arr = [1,2,3,4,5], k = 4, x = 3  
Output: [1,2,3,4]  

Input: arr = [1,2,3,4,5], k = 4, x = -1  
Output: [1,2,3,4]  

Approach (Binary Search + Two Pointers):  
- The array is sorted, so we can use binary search to find  
  the possible insertion point of x.  
- Then, use a sliding window (two pointers) to find the smallest  
  subarray of size k that minimizes distance to x.  
- Alternatively, use binary search directly on the left bound of the window:
  - The possible left bound is between 0 and len(arr) - k.  
  - Compare distance from x to arr[mid] and arr[mid + k].  
  - Move window towards the side with closer elements.  

Time Complexity: O(log(n - k))  
Space Complexity: O(1)
"""

class Solution:
    def findClosestElements(self, arr, k, x):
        left, right = 0, len(arr) - k
        
        while left < right:
            mid = (left + right) // 2
            
            # Compare distances between x and window edges
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        
        return arr[left:left + k]
