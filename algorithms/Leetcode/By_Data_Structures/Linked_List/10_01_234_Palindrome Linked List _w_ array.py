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
Approach 1: Copy into Array List and then Use Two Pointer Technique

Runtime: 1239 ms, faster than 7.57% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 47.2 MB, less than 37.02%

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
        if not head: return head
        curr = head
        pList = []
        while curr:
            pList.append(curr.val)
            curr = curr.next
        return pList == pList[::-1] # This is how to check palindrome in python



