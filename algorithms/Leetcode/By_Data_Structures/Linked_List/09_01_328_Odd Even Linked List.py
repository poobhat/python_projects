"""
Given the head of a singly linked list, group all the nodes with odd indices together
followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it
was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

Constraints:
n == number of nodes in the linked list
0 <= n <= 104
-106 <= Node.val <= 106

"""

"""
Runtime: 63 ms, faster than 6.71% of Python3 online submissions for Odd Even Linked List.
Memory Usage: 16.3 MB, less than 83.67%

Time: O(n)
Space: O(1)

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: [ListNode]) -> [ListNode]:
        if not head: return head # Single node linked list is handled here
        odd = head # As per q, first node is odd
        even = head.next
        evenHead = even # Maintain a separate LL for even nodes.
                        # Odd ones are taken care of in the head only
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead # Link the list of odd nodes with that of even nodes
        return head








