"""
Design your implementation of the linked list. You can choose to use a singly or doubly linked
 list.
A node in a singly linked list should have two attributes: val and next. val is the value of
the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate
the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.

int get(int index) Get the value of the indexth node in the linked list. If the index is
invalid, return -1.

void addAtHead(int val) Add a node of value val before the first element of the linked list.
After the insertion, the new node will be the first node of the linked list.

void addAtTail(int val) Append a node of value val as the last element of the linked list.

void addAtIndex(int index, int val) Add a node of value val before the indexth node in the
linked list. If index equals the length of the linked list, the node will be appended to the
end of the linked list. If index is greater than the length, the node will not be inserted.

void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3

Constraints:

0 <= index, val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.
"""

"""
Singly Linked List using sentinel node

faster than 75.55%
Memory Usage less than 97.59%
"""

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)

    def get(self, index):
        #Return -1 for an invalid index
        if index < 0 or index >= self.size:
            return -1

        #Start with the sentinal head
        curr = self.head
        for _ in range(index+1):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        self.addAtIndex(val,0)

    def addAtTail(self, val):
        self.addAtIndex(val, self.size)

    def addAtIndex(self, val: int, index: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end
        of linked list. If index is greater than the length, the node will not be inserted.
        """

        # If index is greater than the length, the node will not be inserted.
        if index > self.size:
            return

        # [so weird] If index is negative, the node will be inserted at the head of the list.
        if index < 0:
            index = 0

        self.size +=1 # Everytime addAtIndex is called, sized of the linked list is increased by 1
        # find predecessor of the node to be added
        pred = self.head
        for _ in range(index):
            pred = pred.next

        # node to be added
        to_add = ListNode(val)
        # Re-reference the predecessor and its next value with to_add
        to_add.next = pred.next
        pred.next = to_add

    def deleteAtIndex(self, index):
        # Return nothing when an invalid index is passed
        if index < 0 or index >= self.size:
            return

        self.size -= 1 # Everytime deleteAtIndex is called, size is reduced by 1

        # Find the predecessor of the node to be delete
        pred = self.head  # Traversing from the head
        for _ in range(index):
            pred = pred.next

        # delete pred.next
        pred.next = pred.next.next


"""
Complexity Analysis

Time complexity: 
O(1) for addAtHead. 
O(k) for get, addAtIndex, and deleteAtIndex, 
where k is an index of the element to get, add or delete. 
O(N) for addAtTail.

Space complexity: O(1) for all operations.
"""




