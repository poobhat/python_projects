"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0
itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

"""

"""
faster than 13.37%
Memory Usage less than 72.97%

Complexity Analysis

Time complexity : O(max(m,n)). Assume that m and n represents the length of l1 and l2
 respectively, the algorithm above iterates at most max(m,n) times.

Space complexity : O(max(m,n)). The length of the new list is at most max(m,n)+1.

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1:[ListNode], l2:[ListNode]) -> [ListNode]:
        answer_root = curr = ListNode(0)
        carry_over = 0

        while l1 or l2 or carry_over:
            v1, v2 = 0, 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next

            carry_over, first_digit_of_sum = divmod(v1 + v2 + carry_over, 10)

            curr.next = ListNode(first_digit_of_sum)
            curr = curr.next
        return answer_root.next





