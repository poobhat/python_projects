# Definition for a Node.
"""
Runtime: 36 ms, faster than 70.15% of Python3 online submissions for Copy List with Random Pointer.
Memory Usage: 14.9 MB, less than 84.17%
"""
class Node:
    def __init__(self, x: int, next= None, random= None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        if not head: return head

        #weave the linked list with new and old nodes
        curr = head
        while curr:
            currNext = curr.next
            curr.next = Node(curr.val)
            curr.next.next = currNext
            curr = currNext
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        second = curr = head.next
        while curr.next:
            head.next = curr.next
            head = head.next
            curr.next = head.next
            curr = curr.next
        head.next = None
        return second

