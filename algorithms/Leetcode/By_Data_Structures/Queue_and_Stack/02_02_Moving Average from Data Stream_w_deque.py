"""
Approach 2: Double-ended Queue
Intuition
We could do better than the first approach in both time and space complexity.

First of all, one might notice that we do not need to keep all values from the data stream,
but rather the last n values which falls into the moving window.

By definition of the moving window, at each step, we add a new element to the window, and at
the same time we remove the oldest element from the window. Here, we could apply a data
structure called double-ended queue (a.k.a deque) to implement the moving window, which
would have the constant time complexity (O(1)) to add or remove an element
from both its ends. With the deque, we could reduce the space complexity down to
O(N) where N is the size of the moving window.

Secondly, to calculate the sum, we do not need to reiterate the elements in the moving
window.

We could keep the sum of the previous moving window, then in order to obtain the sum of
the new moving window, we simply add the new element and deduce the oldest element. With
this measure, we then can reduce the time complexity to constant.

Algorithm:
Here is the definition of the deque from Python. We have similar implementation of deque in
other programming languages such as Java.

Deques are a generalization of stacks and queues (the name is pronounced deck and is short
for double-ended queue). Deques support thread-safe, memory efficient appends and pops from
either side of the deque with approximately the same O(1) performance in either direction.

Follow the intuition, we replace the queue with the deque and add a new variable window_sum
in order to calculate the sum of moving window in constant time.
"""
import collections

"""
Runtime: 60 ms, faster than 92.53%
Memory Usage: 17.3 MB, less than 61.29%

Complexity: 
Time Complexity: O(1), as we explained in intuition.
Space Complexity: O(N), where NN is the size of the moving window.
"""
from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.maxSize = size
        self.curSize = 0
        self.queue = deque()
        self.windowSum = 0

    def next(self, val: int) -> float:
        self.curSize += 1
        self.queue.append(val)
        frontval = self.queue.popleft() if self.curSize > self.maxSize else 0
        self.windowSum = self.windowSum - frontval + val
        return self.windowSum / min(self.curSize, self.maxSize)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

#######################################################################
"""
Runtime: 189 ms, faster than 7.14%
Memory Usage: 17.2 MB, less than 61.25%
"""
class MovingAverageWithDeque:

    def __init__(self, size: int):
        self.queue = collections.deque(maxlen=size)

    def next(self, val: int) -> float:
        self.queue.append(val)
        return sum(self.queue) / len(self.queue)
