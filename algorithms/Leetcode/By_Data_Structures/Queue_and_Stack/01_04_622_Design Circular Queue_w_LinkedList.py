"""
Approach 2: Singly-Linked List

Intuition:
Similar with Array, the Linked List is another common building block for more
advanced data structures.

Different than a fixed size Array, a linked list could be more memory efficient,
since it does not pre-allocate memory for unused capacity.

With a singly-linked list, we could design a circular queue with the same time and
space complexity as the approach with Array. But we could gain some memory efficiency,
since we don't need to pre-allocate the memory upfront.

Algorithm:
Here we give a list of attributes in our circular queue data structure and the thoughts behind each
attribute.

maxCapacity: the maximum number of elements that the circular queue will hold.
head: the reference to the head element in the queue.
curCapacity: the current length of the queue. This is a critical attribute that helps us to do the
boundary check in each method.
tail: the reference to the tail element in the queue. Unlike the Array approach, we need to explicitly
keep the reference to the tail element. Without this attribute, it would take us O(N) time complexity
to locate the tail element from the head element.

"""

"""
Runtime: 163 ms, faster than 5.18%
Memory Usage: 15 MB, less than 35.28% 

Complexity

Time complexity: \mathcal{O}(1)O(1) for each method in our circular queue.
Space Complexity: The upper bound of the memory consumption for our circular queue 
would be O(N), same as the Array approach. However, it should be more memory efficient
 as we discussed in the intuition section.

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.curCapacity = 0
        self.maxCapacity = k
        self.head = self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        if self.isEmpty():
            self.head = ListNode(value)
            self.tail = self.head
        else:
            newNode = ListNode(value)
            self.tail.next = newNode
            self.tail = newNode
        self.curCapacity += 1
        return True

    def deQueue(self) -> bool:
        if self.isFull(): return False
        self.head = self.head.next
        self.curCapacity -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.head.value

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.tail.value

    def isEmpty(self) -> bool:
        return self.curCapacity == 0

    def isFull(self) -> bool:
        return self.curCapacity == self.maxCapacity

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()