"""
Problem: Smallest Range Covering Elements from K Lists
LeetCode #632
Difficulty: Hard
Link: https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

Problem Statement:
You are given k sorted integer lists.
Find the **smallest range [l, r]** such that the range includes **at least one number from each list**.

Example:
Input:
nums = [
  [4,10,15,24,26],
  [0,9,12,20],
  [5,18,22,30]
]

Possible ranges:
[4,5] → covers list 1 (4), list 3 (5), but not list 2.
[20,24] → covers all lists.
Smallest valid range → [20,24]

Approach: Min-Heap + Tracking Current Max
-----------------------------------------
We push the first element of each list into a min-heap:
    (value, list_index, element_index)

We also keep track of the **current maximum** value among the elements inside the heap.

Algorithm:
1. Initialize:
      - Push (nums[i][0], i, 0) for all lists
      - Track max_value among these
2. Pop the smallest element from heap (min_value).
3. Update best range if (max_value - min_value) is smaller.
4. Move pointer in that list:
      - If next element exists → push to heap
      - Update max_value
      - If no next element → stop (cannot cover all lists anymore)
5. Repeat until one list is exhausted.

Why this works:
- The heap always gives the smallest element among current picks.
- max_value keeps track of the right boundary.
- Ensures each range covers at least one number from each list.

Time Complexity:
- O(N log k), where N = total elements, k = number of lists

Space Complexity:
- O(k) for heap
"""

import heapq

class Solution(object):
    def smallestRange(self, nums):
        k = len(nums)
        min_heap = []
        max_value = float('-inf')

        # Step 1: Initialize heap with first element of each list
        for i in range(k):
            heapq.heappush(min_heap, (nums[i][0], i, 0))
            max_value = max(max_value, nums[i][0])

        best_range = [float('-inf'), float('inf')]

        # Step 2: Pop min and push next from same list
        while True:
            min_value, list_idx, element_idx = heapq.heappop(min_heap)

            # Update best range
            if max_value - min_value < best_range[1] - best_range[0]:
                best_range = [min_value, max_value]

            # Move to next element in the same list
            if element_idx + 1 == len(nums[list_idx]):
                break  # List exhausted → cannot cover all lists anymore

            next_val = nums[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, element_idx + 1))
            max_value = max(max_value, next_val)

        return best_range
