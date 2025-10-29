"""
Problem: Time Based Key-Value Store  
LeetCode #981  
Difficulty: Medium  
Link: https://leetcode.com/problems/time-based-key-value-store/  

Problem Statement:  
Design a time-based key-value data structure that can store multiple values for the same key  
at different timestamps and retrieve the value of a key at a certain timestamp.  

Implement the TimeMap class:
- set(key, value, timestamp): Stores the key with the value at the given timestamp.
- get(key, timestamp): Returns the value such that set was called previously with 
  timestamp_prev <= timestamp. If multiple such values exist, return the one with the largest timestamp_prev.  
  If no values exist, return "".

Examples:  
Input:  
["TimeMap", "set", "get", "get", "set", "get", "get"]  
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]  
Output:  
[None, None, "bar", "bar", None, "bar2", "bar2"]

Approach (Binary Search per Key):  
- Use a dictionary to map each key → list of (timestamp, value) pairs.  
- For `set`, append the (timestamp, value) since timestamps are strictly increasing.  
- For `get`, perform binary search on timestamps to find the largest timestamp ≤ given timestamp.  

Time Complexity:  
- set: O(1)  
- get: O(log n) per query  

Space Complexity: O(n)
"""

class TimeMap:
    def __init__(self):
        self.store = {}  # key -> list of (timestamp, value)

    def set(self, key, value, timestamp):
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key, timestamp):
        if key not in self.store:
            return ""

        pairs = self.store[key]
        left, right = 0, len(pairs) - 1
        res = ""

        # Binary search for the largest timestamp <= given timestamp
        while left <= right:
            mid = (left + right) // 2
            if pairs[mid][0] <= timestamp:
                res = pairs[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return res
