'''
Problem: Exam Room
LeetCode #855
Difficulty: Medium
Link: https://leetcode.com/problems/exam-room/

Problem Statement:
You are given an exam room with N seats in a single row, numbered from 0 to N-1.

When a student enters, they must sit in a seat such that the distance to the closest occupied seat is maximized.
If there are multiple such seats, choose the seat with the smallest index.

When a student leaves, the seat becomes empty.

You need to implement the ExamRoom class with the following methods:
- seat(): returns the seat number the student sits in
- leave(p): removes the student sitting at seat p

Examples:
ExamRoom(10)
seat() → 0
seat() → 9
seat() → 4
seat() → 2
leave(4)
seat() → 5

Approach:
Maintain a sorted list of currently occupied seats.
For every new student, check:
- Distance from the first occupied seat to seat 0
- Distance between every pair of adjacent occupied seats (midpoint)
- Distance from the last occupied seat to seat N-1
Choose the seat that maximizes the minimum distance to the closest student.

Algorithm:
1. Initialize an empty list to store occupied seats.
2. For seat():
   - If no seats are occupied, seat the student at position 0.
   - Set maxDist to distance from seat 0 to the first occupied seat.
   - Iterate through adjacent occupied seats:
       - Compute midpoint distance = (current - previous) // 2
       - Update the best seat if this distance is greater.
   - Check distance from the last occupied seat to N-1.
   - Insert the chosen seat into the list and keep it sorted.
   - Return the chosen seat.
3. For leave(p):
   - Remove p from the occupied seats list.

Why this works?
- The maximum minimum distance can only occur at:
  - One of the room edges, or
  - The midpoint between two occupied seats
- Checking all these positions guarantees the optimal seat choice.
- Keeping the seats sorted ensures correct distance calculations.

Time Complexity:
- seat(): O(n), where n is the number of occupied seats
- leave(): O(n) due to list removal

Space Complexity:
- O(n) for storing occupied seats
'''

import bisect

class ExamRoom(object):
    def __init__(self, n):
        self.n = n
        self.seats = []  # sorted list of occupied seats

    def seat(self):
        # If no one is seated, take seat 0
        if not self.seats:
            self.seats.append(0)
            return 0

        max_dist = self.seats[0]  # distance from 0 to first occupied
        seat_to_take = 0

        # Check distances between occupied seats
        for i in range(1, len(self.seats)):
            prev = self.seats[i - 1]
            curr = self.seats[i]
            dist = (curr - prev) // 2
            if dist > max_dist:
                max_dist = dist
                seat_to_take = prev + dist

        # Check distance from last occupied seat to end
        last_dist = (self.n - 1) - self.seats[-1]
        if last_dist > max_dist:
            seat_to_take = self.n - 1

        bisect.insort(self.seats, seat_to_take)
        return seat_to_take

    def leave(self, p):
        self.seats.remove(p)