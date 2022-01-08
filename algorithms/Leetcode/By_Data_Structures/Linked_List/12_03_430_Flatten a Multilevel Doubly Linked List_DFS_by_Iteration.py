"""
Iteration - simpler approach

Runtime: 36 ms, faster than 69.81% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.
Memory Usage: 14.6 MB, less than 84.94%
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution(object):
    def getTail(self, node):
        subHead = node
        while subHead.next:
            subHead=subHead.next
        return subHead

    def flatten(self, head):
        if not head: return
        temp = head
        while temp:
            if temp.child:
                originalTempNext = temp.next
                temp.next = temp.child
                temp.child.prev = temp
                subListTail = self.getTail(temp.child)
                subListTail.next = originalTempNext
                if originalTempNext:
                    originalTempNext.prev = subListTail
                temp.child = None
            temp = temp.next
        return head
