"""
Approach 3: Circular Queue with Array
Intuition
Other than the deque data structure, one could also apply another fun data structure called
circular queue, which is basically a queue with the circular shape.
The major advantage of circular queue is that by adding a new element to a full circular
queue, it automatically discards the oldest element. Unlike deque, we do not need to
explicitly remove the oldest element.
Another advantage of circular queue is that a single index suffices to keep track of both
ends of the queue, unlike deque where we have to keep a pointer for each end.
Algorithm

No need to resort to any library, one could easily implement a circular queue with a
fixed-size array. The key to the implementation is the correlation between the index of
head and tail elements, which we could summarize in the following formula:

tail=(head+1) mod size

In other words, the tail element is right next to the head element. Once we move the head
forward, we would overwrite the previous tail element.
"""
"""
Runtime: 69 ms, faster than 69.23%
Memory Usage: 17.2 MB, less than 85.53% 
"""
class MovingAverage:

    def __init__(self, size: int):
        self.queue = [0]*size
        self.maxSize = size
        self.currSize = 0
        self.head = 0
        self.windowSum = 0

    def next(self, val: int) -> float:
        self.currSize += 1
        front = self.queue[self.head]
        self.windowSum = self.windowSum - front + val
        self.head = (self.head + 1) % self.maxSize
        tail = (self.head + self.maxSize - 1) % self.maxSize
        self.queue[tail] = val

        return self.windowSum/min(self.currSize, self.maxSize)








# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)