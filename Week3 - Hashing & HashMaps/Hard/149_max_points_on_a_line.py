"""
Problem: Max Points on a Line  
LeetCode #149  
Difficulty: Hard  
Link: https://leetcode.com/problems/max-points-on-a-line/  

Problem Statement:  
Given an array of points where points[i] = [xi, yi] represents a point on the XY plane,  
return the maximum number of points that lie on the same straight line.

Examples:  
Input: points = [[1,1],[2,2],[3,3]]  
Output: 3  

Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]  
Output: 4  

Approach:  
- For each point, calculate the slope it forms with every other point.  
- Normalize slopes using the ratio dy/dx in its reduced form to handle precision.  
- Handle vertical lines (dx = 0) and horizontal lines (dy = 0) separately.  
- Count how many points share the same slope from the current point.  
- Track the maximum count across all starting points.  

Note:  
- Since we can’t use libraries, we’ll manually compute GCD to simplify slope ratios.  

Time Complexity: O(n²)  
Space Complexity: O(n)
"""

class Solution:
    def maxPoints(self, points):
        if len(points) <= 2:
            return len(points)

        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        result = 0
        for i in range(len(points)):
            slopes = {}
            duplicates = 1
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]

                dx = x2 - x1
                dy = y2 - y1

                if dx == 0 and dy == 0:
                    duplicates += 1
                    continue

                if dx == 0:
                    slope = ('inf', 0)
                elif dy == 0:
                    slope = (0, 'inf')
                else:
                    g = gcd(dy, dx)
                    dy //= g
                    dx //= g
                    # Ensure consistent direction for slope
                    if dx < 0:
                        dx, dy = -dx, -dy
                    slope = (dy, dx)

                if slope in slopes:
                    slopes[slope] += 1
                else:
                    slopes[slope] = 1

            current_max = duplicates
            for slope in slopes:
                if slopes[slope] + duplicates > current_max:
                    current_max = slopes[slope] + duplicates

            if current_max > result:
                result = current_max

        return result
