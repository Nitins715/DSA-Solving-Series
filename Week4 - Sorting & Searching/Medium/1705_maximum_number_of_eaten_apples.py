"""
Problem: Maximum Number of Eaten Apples  
LeetCode #1705  
Difficulty: Medium  
Link: https://leetcode.com/problems/maximum-number-of-eaten-apples/  

Problem Statement:  
There is a tree that grows apples every day for n days.  
On the i-th day, the tree produces apples[i] apples,  
and these apples will rot after days[i] days.  

You can eat at most one apple per day.  
Return the maximum number of apples you can eat before they rot.  

Examples:  
Input: apples = [1,2,3,5,2], days = [3,2,1,4,2]  
Output: 7  

Input: apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2]  
Output: 5  

Approach (Min-Heap / Greedy Simulation):  
- Each day, new apples are produced and added to a heap with their expiration day.  
- Each heap element = (expiry_day, count_of_apples).  
- On each day:
  1. Remove all expired apples from the heap (expiry_day <= today).  
  2. Add new apples (if any) with expiry_day = today + days[i].  
  3. Eat one apple from the batch that expires the earliest (heap top).  
- Continue simulation even after all days are done if unrotten apples remain.  

Time Complexity: O(n log n)  
Space Complexity: O(n)
"""

import heapq

class Solution:
    def eatenApples(self, apples, days):
        heap = []  # (expiry_day, apple_count)
        eaten = 0
        day = 0
        n = len(apples)

        while day < n or heap:
            # Remove rotten apples
            while heap and heap[0][0] <= day:
                heapq.heappop(heap)

            # Add today's apples
            if day < n and apples[day] > 0:
                heapq.heappush(heap, (day + days[day], apples[day]))

            # Eat one apple from the batch that expires earliest
            if heap:
                expiry, count = heapq.heappop(heap)
                eaten += 1
                if count > 1:
                    heapq.heappush(heap, (expiry, count - 1))

            day += 1

        return eaten
