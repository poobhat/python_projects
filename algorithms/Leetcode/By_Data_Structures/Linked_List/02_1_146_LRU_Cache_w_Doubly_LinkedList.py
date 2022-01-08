"""
Design a data structure that follows the constraints of a Least Recently Used (LRU)
cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.

int get(int key) Return the value of the key if the key exists, otherwise return -1.

void put(int key, int value) Update the value of the key if the key exists. Otherwise,
add the key-value pair to the cache. If the number of keys exceeds the capacity from
this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4


Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.

"""

"""
Approach 2: Hashmap + DoubleLinkedList

Time complexity : O(1) both for put and get.

Space complexity : O(capacity) since the space is used only for a hashmap and
double linked list with at most capacity + 1 elements.

"""

# _add_node, _remove_node, _move_to_head, _pop_tail

class ListNode:

    def __init__(self):
        self.key = 0
        self.value = 0
        self.next = None
        self.prev = None
        a = 22
        a.__sizeof__()

class LRUCache:

    def __init__(self, capacity):
        self.size = 0
        self.head, self.tail = ListNode(), ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.cache = {}
        self.capacity = capacity

    def _add_node(self, node):
        pred = self.head
        succ = self.head.next

        node.prev = pred
        node.next = succ
        pred.next = node
        succ.prev = node

    def _remove_node(self, node):
        pred = node.prev
        succ = node.next

        pred.next = succ
        succ.prev = pred

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        tail = self.tail.prev
        self._remove_node(tail)
        return tail

    def get(self, key):
        node = self.cache.get(key)
        if not node:
            return -1
        self._move_to_head(node)
        return node.value

    def put(self, key, value):
        node = self.cache.get(key)
        if not node:
            newNode = ListNode()
            newNode.key = key
            newNode.value = value

            self.cache[key] = newNode
            self._add_node(newNode)

            self.size += 1

            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.value = value
            self._move_to_head(node)
