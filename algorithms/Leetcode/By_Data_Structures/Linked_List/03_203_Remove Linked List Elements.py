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
Runtime: 84 ms, faster than 9.92% 
Memory Usage: 18.8 MB, less than 9.25%.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: [ListNode], val: int) -> [ListNode]:

        answer_root = curr = ListNode(0)

        while head:
            if head.val != val:
                curr.next = ListNode(head.val)
                curr = curr.next
            head = head.next

        return answer_root.next



