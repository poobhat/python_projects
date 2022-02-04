"""
Given the head of a singly linked list, return true if it is a palindrome.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

Constraints:
The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
"""
"""
Approach 2: Recursive (Advanced)

Runtime: Runtime: 1016 ms, faster than 43.49%
Memory Usage: Memory Usage: 128.6 MB, less than 5.06%

Time:  O(2n) == O(n)
Space: O(n)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: [ListNode]) -> bool:
        self.ptr1 = head

        def recursively_check(curr = head):
            if curr:
                if not recursively_check(curr.next):
                    return False
                if self.ptr1.val != curr.val:
                    return False
                self.ptr1 = self.ptr1.next
            return True

        return recursively_check()


