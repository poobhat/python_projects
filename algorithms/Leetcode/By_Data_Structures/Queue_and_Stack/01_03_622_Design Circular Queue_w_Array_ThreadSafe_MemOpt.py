"""
Improvement: Thread-Safe

One might be happy with the circular queue with array implementation, after all it
meets all the requirements of the problem.

As a followup question though, an interviewer might ask one to point out a potential
defect about the implementation and the solution.

This time, it is not about the space or time complexity, but concurrency. Our circular
queue is NOT thread-safe. One could end up with corrupting our data structure in a
 multi-threaded environment.

This scenario is called race conditions as described in the problem of Print in Order.
One can find more concurrency problems to practice on LeetCode.
https://leetcode.com/problemset/concurrency/

"""


"""
Runtime: 112 ms, faster than 23.92% of Python3 online submissions for Design Circular Queue.
Memory Usage: 14.9 MB, less than 63.36%
Complexity

Time complexity: O(1). All of the methods in our circular data structure is of
constant time complexity.
Space Complexity: O(N). The overall space complexity of the data structure is linear,
where NN is the pre-assigned capacity of the queue. However, it is worth mentioning
that the memory consumption of the data structure remains as its pre-assigned capacity
during its entire life cycle.
"""

from threading import Lock
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0]*k
        self.currCapacity = 0
        self.maxCapacity = k
        self.head = self.tail = -1
        self.queueLock = Lock()

    def enQueue(self, value: int) -> bool:
        with self.queueLock:
            if self.isFull(): return False
            if self.tail == -1:
                self.head = self.tail = 0
            else:
                self.tail = (self.tail + 1) % self.maxCapacity
            self.queue[self.tail] = value
            self.currCapacity += 1
        return True

    def deQueue(self) -> bool:
        with self.queueLock:
            if self.isEmpty(): return False
            if self.tail == self.head:
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