"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together
the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

"""
Time complexity : O(n + m)O(n+m)

Because exactly one of l1 and l2 is incremented on each loop iteration, the while loop runs for a number 
of iterations equal to the sum of the lengths of the two lists. All other work is constant, so the overall 
complexity is linear.

Space complexity : O(1)O(1)

The iterative approach only allocates a few pointers, so it has a constant overall memory footprint.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:

        if not list1: return list2
        if not list2: return list1
        answer = ListNode(-1)

        while list1 and list2:
            if list1.val <= list2.val:
                answer.next = list1
                list1 = list1.next
            elif list2.val < list1.val:
                answer.next = list2
                list2 = list2.next

        answer.next = list1 if list1 else list2

        return answer.next

