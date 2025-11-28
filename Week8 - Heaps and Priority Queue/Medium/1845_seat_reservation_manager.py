"""
Problem: Seat Reservation Manager
LeetCode #1845
Difficulty: Medium
Link: https://leetcode.com/problems/seat-reservation-manager/

Problem Statement:
Design a system that:
- Manages seat reservations for seats numbered from 1 to n.
- Supports two operations:
    1. reserve() → Reserves the smallest-numbered unreserved seat, returns the seat number.
    2. unreserve(seatNumber) → Frees the given seat so it becomes available again.

Example:
Input:
n = 5
reserve() → 1
reserve() → 2
unreserve(2)
reserve() → 2
reserve() → 3
reserve() → 4
reserve() → 5
reserve() → (none available, but constraints guarantee valid calls)

Approach:
Use a **min-heap** to always retrieve the smallest available seat.

Steps:
1. Initialize a min-heap with all seat numbers 1…n.
2. On reserve():
      - Pop the smallest number from the heap.
3. On unreserve(seatNumber):
      - Push seatNumber back into the heap.

Why min-heap?
- Efficiently tracks the smallest available seat.
- reserve() → O(log n)
- unreserve() → O(log n)

Time Complexity:
- Initialization: O(n)
- reserve/unreserve: O(log n)

Space Complexity:
- O(n) for heap
"""

import heapq

class SeatManager(object):

    def __init__(self, n):
        # Initialize min-heap with all seat numbers
        self.heap = [i for i in range(1, n + 1)]
        heapq.heapify(self.heap)

    def reserve(self):
        # Always pop the smallest available seat
        return heapq.heappop(self.heap)

    def unreserve(self, seatNumber):
        # Push seat back into heap
        heapq.heappush(self.heap, seatNumber)
