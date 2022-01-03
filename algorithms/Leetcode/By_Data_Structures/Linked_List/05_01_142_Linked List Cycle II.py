"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle,
return null.

There is a cycle in a linked list if there is some node in the list that can be reached
again by continuously following the next pointer. Internally, pos is used to denote the
index of the node that tail's next pointer is connected to (0-indexed).
It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.


Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.

"""
"""
Runtime: 63 ms, faster than 19.39% of Python3 online submissions for Linked List Cycle II.
Memory Usage: 17.3 MB, less than 55.94% of Python3 online submissions 

Complexity Analysis

Time complexity : O(n)
For cyclic lists, hare and tortoise will point to the same node after F+C−h iterations, 
as demonstrated in the proof of correctness. F+C−h ≤ F+C=n, so phase 1 runs 
in O(n) time. Phase 2 runs for F<n iterations, so it also runs in O(n) time.

For acyclic lists, hare will reach the end of the list in roughly n/2 
iterations, causing the function to return before phase 2. 
Therefore, regardless of which category of list the algorithm receives, 
it runs in time linearly proportional to the number of nodes.

Space complexity : O(1)
Floyd's Tortoise and Hare algorithm allocates only pointers, so it runs with constant 
overall memory usage.

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle1(self, head: [ListNode]) -> [ListNode]:

        slow = head
        fast = head

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                ptr1 = head
                ptr2 = fast

                while ptr1 is not ptr2:
                    ptr1 = ptr1.next
                    ptr2 = ptr2.next

                return ptr1
        return None
    """
    Runtime: 48 ms, faster than 82.23% of Python3 online submissions for Linked List Cycle II.
    Memory Usage: 17.2 MB, less than 55.94% of Python3 online submissions.
    """
    def detectCycle2(self, head: [ListNode]) -> [ListNode]:

        try:
            fast = head.next
            slow = head
            while fast is not slow:
                fast = fast.next.next
                slow = slow.next
        except:
            # if there is an exception, we reach the end and there is no cycle
            return None

        # since fast starts at head.next, we need to move slow one step forward
        slow = slow.next
        while head is not slow:
            head = head.next
            slow = slow.next

        return head


