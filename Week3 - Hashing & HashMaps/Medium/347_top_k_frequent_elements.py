"""
Problem: Top K Frequent Elements  
LeetCode #347  
Difficulty: Medium  
Link: https://leetcode.com/problems/top-k-frequent-elements/  

Problem Statement:  
Given an integer array nums and an integer k,  
return the k most frequent elements.  
You may return the answer in any order.

Examples:  
Input: nums = [1,1,1,2,2,3], k = 2  
Output: [1,2]  

Input: nums = [1], k = 1  
Output: [1]  

Approach (Frequency Counting + Sorting):  
- Create a dictionary to store the frequency of each element.  
- Sort the dictionary keys by their frequency in descending order.  
- Return the first k elements from the sorted result.  
- This approach avoids using libraries like collections or heapq.

Time Complexity: O(n log n), due to sorting  
Space Complexity: O(n), for frequency storage
"""

class Solution:
    def topKFrequent(self, nums, k):
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # sort keys based on frequency (highest first)
        sorted_keys = sorted(freq, key=lambda x: freq[x], reverse=True)

        # return top k elements
        return sorted_keys[:k]
