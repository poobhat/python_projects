"""
Given the head of a linked list, remove the nth node from the end of the list and
return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""
"""
Single pass algorithm - 2 pointer

Time: O(n)
Space: O(1)

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def removeNthFromEnd1(self, head: [ListNode], n: int) -> [ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first, second = dummy, dummy
        for _ in range(n+1): # move the first pointer n places ahead.
            first = first.next
        while first: # When the first pointer have reached the end of the linked list,
                     # the second pointer will have reached the nth position from the end
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
    """
    Runtime: 28 ms, faster than 95.87% of Python3 online submissions for Remove Nth Node From End of List.
    Memory Usage: 13.9 MB, less than 92.09%
    """
    def removeNthFromEnd3(self, head: [ListNode], n: int) -> [ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = head
        for _ in range(n):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next

    """
    Runtime: 39 ms, faster than 23.54% of Python3 online submissions for Remove Nth Node From End of List.
    Memory Usage: 14.3 MB, less than 49.33%
    """

    def removeNthFromEnd2(self, head: [ListNode], n: int) -> [ListNode]:
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        while not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

    """
    Runtime: 28 ms, faster than 93.07% of Python3 online submissions.
    Memory Usage: 14.3 MB, less than 49.17% of Python3 online submissions.
    """
    def removeNthFromEnd4(self, head: [ListNode], n: int) -> [ListNode]:
        def remove(head):
            if not head:
                return 0, head
            i, head.next = remove(head.next)
            return i+1, (head, head.next)[i+1 == n]
        return remove(head)[1]

