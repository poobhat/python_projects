"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list
that has Node.val == val, and return the new head.
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []
Example 3:

Input: head = [7,7,7,7], val = 7
Output: []

"""
"""
Recursion

Runtime: 97 ms, faster than 35.89%
Memory Usage: 27 MB, less than 5.13% 

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: [ListNode], val: int) -> [ListNode]:
        def rec(node, val):
            if node:
                if node.val == val:
                    return rec(node.next, val)
                else:
                    node.next = rec(node.next, val)
            return node
        return rec(head, val)







