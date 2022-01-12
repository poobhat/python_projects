"""
Runtime: 28 ms, faster than 97.23% of Python3 online submissions for Copy List with
Random Pointer.
Memory Usage: 15.1 MB, less than 44.23%

Time Complexity : O(N) because we make one pass over the original linked list.
Space Complexity : O(N) as we have a dictionary containing mapping from old list nodes
to new list nodes. Since there are NN nodes, we have O(N) space complexity.

"""

class Node:
    def __init__(self, x: int, next = None, random = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def __init__(self):
        self.visited = {}

    def getNode(self, node):
        if node:
            newNode = Node(node.val)
            if node not in self.visited:
                self.visited[node] = newNode
            return self.visited[node]
        return None

    def copyRandomList(self, head):
        if not head: return head
        oldNode = head
        newNode = Node(oldNode.val)
        self.visited[oldNode] = newNode
        while oldNode:
            newNode.next = self.getNode(oldNode.next)
            newNode.random = self.getNode(oldNode.random)
            oldNode = oldNode.next
            newNode = newNode.next
        return self.visited[head]

