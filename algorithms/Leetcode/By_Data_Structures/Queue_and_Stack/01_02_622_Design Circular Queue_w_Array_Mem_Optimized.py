"""
Runtime: 93 ms, faster than 37.85% of Python3 online submissions for Design Circular Queue.
Memory Usage: 14.7 MB, less than 95.74%
"""

class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0]*k
        self.currCapacity = 0
        self.maxCapacity = k
        self.head = self.tail = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        if self.tail == -1:
            self.head = self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.maxCapacity
        self.queue[self.tail] = value
        self.currCapacity += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        if self.head == self.tail:
            self.head = self.tail = -1
        else:
            self.head = (self.head + 1) % self.maxCapacity
        self.currCapacity -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.head]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.tail]

    def isEmpty(self) -> bool:
        return self.currCapacity == 0

    def isFull(self) -> bool:
        return self.currCapacity == self.maxCapacity

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()