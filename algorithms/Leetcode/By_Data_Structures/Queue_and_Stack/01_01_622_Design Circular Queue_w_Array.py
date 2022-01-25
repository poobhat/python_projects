"""
Design your implementation of the circular queue. The circular queue is a linear data
structure in which the operations are performed based on FIFO (First In First Out) principle
and the last position is connected back to the first position to make a circle. It is also
called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of
the queue. In a normal queue, once the queue becomes full, we cannot insert the next element
even if there is a space in front of the queue. But using the circular queue, we can use the
space to store new values.

Implementation the MyCircularQueue class:

MyCircularQueue(k) Initializes the object with the size of the queue to be k.
int Front() Gets the front item from the queue. If the queue is empty, return -1.
int Rear() Gets the last item from the queue. If the queue is empty, return -1.
boolean enQueue(int value) Inserts an element into the circular queue. Return true if the
operation is successful.
boolean deQueue() Deletes an element from the circular queue. Return true if the operation is
successful.
boolean isEmpty() Checks whether the circular queue is empty or not.
boolean isFull() Checks whether the circular queue is full or not.
You must solve the problem without using the built-in queue data structure in your programming
language.

Example 1:
Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue",
"enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4

Constraints:
1 <= k <= 1000
0 <= value <= 1000
At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.
"""
"""
With the formula ::
tailIndex = (headIndex + queueLength - 1) % arrayCapacity
"""

"""
Runtime: 114 ms, faster than 21.87% of Python3 online submissions for Design Circular Queue.
Memory Usage: 14.8 MB, less than 85.56%
"""

"""
Time complexity: O(1). All of the methods in our circular data structure is of constant time
 complexity.
 
Space Complexity: O(N). The overall space complexity of the data structure is linear,
where NN is the pre-assigned capacity of the queue. However, it is worth mentioning that
the memory consumption of the data structure remains as its pre-assigned capacity during
its entire life cycle.
"""

"""
*****************************!!!!!!!!!!!!!!!
Our circular queue is NOT thread-safe. One could end up with corrupting our 
data structure in a multi-threaded environment
"""

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [0]*k
        self.qSize = 0
        self.qMaxSize = k
        self.headIndex = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull(): return False
        self.queue[(self.headIndex + self.qSize) % self.qMaxSize] = value
        self.qSize += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty(): return False
        self.headIndex = (self.headIndex + 1) % self.qMaxSize
        self.qSize -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return -1 if self.isEmpty() else self.queue[self.headIndex]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return -1 if self.isEmpty() else self.queue[(self.headIndex + self.qSize - 1) % self.qMaxSize]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.qSize == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.qSize == self.qMaxSize

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()