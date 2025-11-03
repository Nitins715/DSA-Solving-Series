"""
Problem: Design Linked List  
LeetCode #707  
Difficulty: Medium  
Link: https://leetcode.com/problems/design-linked-list/  

Problem Statement:  
Design your implementation of the linked list.  
You can choose to use a singly or doubly linked list.  

Implement the following methods:
- get(index): Get the value of the index-th node in the linked list. If the index is invalid, return -1.  
- addAtHead(val): Add a node of value val before the first element of the linked list.  
- addAtTail(val): Append a node of value val to the last element of the linked list.  
- addAtIndex(index, val): Add a node of value val before the index-th node in the linked list.  
  If index equals the length of the linked list, the node will be appended to the end.  
  If index is greater than the length, the node will not be inserted.  
- deleteAtIndex(index): Delete the index-th node in the linked list if the index is valid.  

Examples:  
Input:  
["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]  
[[],[1],[3],[1,2],[1],[1],[1]]  

Output:  
[null,null,null,null,2,null,3]  

Approach (Singly Linked List Implementation):  
- Maintain a `head` pointer and a variable `size` to track list length.  
- Traverse nodes as needed for `get`, `addAtIndex`, and `deleteAtIndex`.  
- Carefully handle edge cases for insertion and deletion at head/tail positions.  

Time Complexity:  
- get: O(n)  
- addAtHead / addAtTail: O(1) / O(n)  
- addAtIndex / deleteAtIndex: O(n)  
Space Complexity: O(n)
"""

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if not self.head:
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
        node = Node(val)
        node.next = curr.next
        curr.next = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next
        self.size -= 1
