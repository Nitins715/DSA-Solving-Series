"""
Problem: Random Pick with Weight  
LeetCode #528  
Difficulty: Medium  
Link: https://leetcode.com/problems/random-pick-with-weight/  

Problem Statement:  
You are given a list of positive integers w where w[i] describes the weight of index i (0-indexed).  
We need to randomly pick an index in proportion to its weight.

More formally, the probability of picking index i is w[i] / sum(w).

Examples:  
Input: ["Solution","pickIndex","pickIndex","pickIndex"], [[[1,3]],[],[],[]]  
Output: [null,1,1,1]  
Explanation: The probability of picking index 1 is 3/4,  
while index 0 has probability 1/4.

Approach (Prefix Sum + Binary Search):  
- Precompute a prefix sum array where each element stores cumulative weights.  
- To pick an index, generate a random number between 1 and total weight.  
- Use binary search to find the smallest prefix >= random number.  
- That index is returned.

Time Complexity:  
- Constructor: O(n)  
- pickIndex: O(log n)  

Space Complexity: O(n)
"""

import random

class Solution:
    def __init__(self, w):
        self.prefix = []
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)
        self.total = total

    def pickIndex(self):
        target = random.randint(1, self.total)
        low, high = 0, len(self.prefix) - 1

        # binary search for the first prefix >= target
        while low < high:
            mid = (low + high) // 2
            if target > self.prefix[mid]:
                low = mid + 1
            else:
                high = mid
        return low
