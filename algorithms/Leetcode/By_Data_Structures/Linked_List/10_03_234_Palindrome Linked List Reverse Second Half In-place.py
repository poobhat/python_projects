"""
Runtime: 1384 ms, faster than 5.01% of Python3 online submissions for Palindrome Linked
List.
Memory Usage: 47.3 MB, less than 37.02%
"""

class Solution:
    def isPalindrome(self, head):
        firstHalf = None
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            # Key to reversing linked list in place
            firstHalf, firstHalf.next, head  = head, firstHalf, head.next
        secondHalf = head.next if fast else head

        isPali = True
        while firstHalf:
            isPali = isPali if firstHalf.val == secondHalf.val else False
            head, head.next, firstHalf = firstHalf, head, firstHalf.next
            secondHalf = secondHalf.next
        return isPali

