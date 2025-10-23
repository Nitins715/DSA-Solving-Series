"""
Problem: Find Duplicate Subtrees  
LeetCode #652  
Difficulty: Medium  
Link: https://leetcode.com/problems/find-duplicate-subtrees/  

Problem Statement:  
Given the root of a binary tree, return all duplicate subtrees.  
For each kind of duplicate subtree, you only need to return the root node of any one of them.

Two trees are considered duplicate if they have the same structure and the same node values.

Examples:  
Input: root = [1,2,3,4,null,2,4,null,null,4]  
Output: [[2,4],[4]]  

Approach (Tree Serialization + Hashing):  
- Perform a postorder traversal of the tree.  
- For each node, serialize it as a string in the form:  
  "value,left_serial,right_serial".  
- Use a dictionary to count how many times each serialized subtree appears.  
- When a subtree’s serialization appears for the second time, record its root node.  
- Finally, return the list of duplicate subtree roots.

Time Complexity: O(n), where n is the number of nodes  
Space Complexity: O(n), for storing subtree serializations
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root):
        seen = {}
        duplicates = []

        def serialize(node):
            if not node:
                return "#"
            serial = str(node.val) + "," + serialize(node.left) + "," + serialize(node.right)

            if serial in seen:
                seen[serial] += 1
                if seen[serial] == 2:
                    duplicates.append(node)
            else:
                seen[serial] = 1

            return serial

        serialize(root)
        return duplicates
