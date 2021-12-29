"""
Implement a doubly Linked List
"""
"""
faster than 93.39%
Memory Usage less than 5.59%

Time complexity: O(1) for addAtHead and addAtTail. 
O(min(k,N−k)) for get, addAtIndex, and deleteAtIndex, 
where k is an index of the element to get, add or delete.

Space complexity: O(1) for all operations.
"""

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head, self.tail = ListNode(0), ListNode(0)
        self.size = 0
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1

        if index+1 < self.size - index:
            curr = self.head
            for _ in range(index+1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev
        return curr.val

    def addAtHead(self, val):
        pred = self.head
        succ = self.head.next

        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add

    def addAtTail(self, val):
        succ = self.tail
        pred = self.tail.prev

        self.size += 1
        to_add = ListNode(val)
        to_add.next = succ
        to_add.prev = pred
        succ.prev = to_add
        pred.next = to_add


    def addAtIndex(self, index, val):
        if index > self.size:
            return
        if index < 0:
            index = 0

        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next
        else:
            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev

        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add

    def deleteAtIndex(self, index):

        if index < 0 or index >= self.size:
            return

        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next
        else:
            succ = self.tail
            for _ in range(self.size - index - 1):
                succ = succ.prev
            pred = succ.prev.prev

        self.size -= 1
        pred.next = succ
        succ.prev = pred













