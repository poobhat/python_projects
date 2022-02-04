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

"""
Runtime: 854 ms, faster than 80.26%
Memory Usage: 75.5 MB, less than 71.86%
"""
from collections import OrderedDict

class LRUCache(OrderedDict):
    def __init__(self, capacity):
        super().__init__()
        self.size = capacity

    def get(self, key):
        if key not in self: return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key, val):
        if key in self: del self[key]
        self[key] = val
        if len(self) > self.size:
            self.popitem(last=False)
