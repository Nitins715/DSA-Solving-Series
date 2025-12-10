"""
Problem: Serialize and Deserialize Binary Tree
LeetCode #297
Difficulty: Hard
Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Problem Statement:
Design an algorithm to convert a binary tree into a string (serialize)  
and convert the string back into the same binary tree (deserialize).

Constraints:
- The structure and node values must be preserved exactly.
- Null children must also be represented.

Example:
Input Tree:
    1
   / \
  2   3
     / \
    4   5

Serialized: "1,2,None,None,3,4,None,None,5,None,None"

Approach: Preorder Traversal (DFS)
----------------------------------
Serialization:
- Use preorder traversal: Node → Left → Right
- If node is None → append "None"
- Otherwise append its value
- Join list with commas

Deserialization:
- Read values using an iterator
- If value = "None", return None
- Otherwise create a node and recursively build left and right children

Why this works:
- Preorder with explicit "None" markers uniquely reconstructs the tree.

Time Complexity:
- O(n) serialize
- O(n) deserialize

Space Complexity:
- O(n) for output string and recursion stack
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        res = []

        def dfs(node):
            if not node:
                res.append("None")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        values = iter(data.split(","))

        def dfs():
            val = next(values)
            if val == "None":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
