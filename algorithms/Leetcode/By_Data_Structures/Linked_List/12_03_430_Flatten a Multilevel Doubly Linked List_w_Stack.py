# Definition for a Node.
"""
Runtime: 28 ms, faster than 96.77% of Python3 online submissions for
Flatten a Multilevel Doubly Linked List.
Memory Usage: 14.9 MB, less than 45.10%
"""
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution(object):
    def flatten(self, head):
        if not head: return
        previous = Node(0)
        stack = [head]

        while stack:
            current = stack.pop()
            current.prev = previous
            previous.next = current
            if current.next: # when current.next becomes null, stack will pop the original next nodes from the
                stack.append(current.next)
            if current.child: # Always keeps the child on top of the stack
                stack.append(current.child)
                current.child = None # Makes sure that the we don't reprocess the already visited child node again
            previous=current

        head.prev = None
        return head


