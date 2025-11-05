"""
Problem: Merge k Sorted Lists  
LeetCode #23  
Difficulty: Hard  
Link: https://leetcode.com/problems/merge-k-sorted-lists/  

Problem Statement:  
You are given an array of k linked lists, each of which is sorted in ascending order.  
Merge all the linked lists into one sorted linked list and return it.  

Examples:  
Input: lists = [[1,4,5],[1,3,4],[2,6]]  
Output: [1,1,2,3,4,4,5,6]  

Input: lists = []  
Output: []  

Input: lists = [[]]  
Output: []  

Approach (Min-Heap / Priority Queue - Optimized):  
1. Use a min-heap to efficiently get the smallest node among k lists.  
2. Push the first node of each non-empty list into the heap along with its index.  
3. Pop the smallest element, append it to the merged list, and push its next node if it exists.  
4. Continue until the heap is empty.  

This efficiently merges k sorted lists with minimal comparisons.

Time Complexity: O(N log k) — where N is total nodes, k is number of lists.  
Space Complexity: O(k) — for the heap.
"""

import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        if not lists or len(lists) == 0:
            return None

        heap = []
        # Step 1: Initialize heap with first node of each list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        curr = dummy

        # Step 2: Process heap
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
