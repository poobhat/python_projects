"""
Given the head of a linked list, remove the nth node from the end of the list and
return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""
"""
Two pass algorithm - 1 pointer

Time: O(m+m-n) == O(m) where m is the length of the linked list
Space: O(1)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        length = 0

        # First pass to the end
        while curr: # Calculate the length of the linked list
            length += 1
            curr = curr.next

        length -= n # Calculate the index of the node to be removed

        curr = dummy # Start from the beginning again

        # Second pass up-to the node to be removed
        while length > 0:
            length -= 1
            curr = curr.next
        curr.next = curr.next.next # Unlink

        return dummy.next



