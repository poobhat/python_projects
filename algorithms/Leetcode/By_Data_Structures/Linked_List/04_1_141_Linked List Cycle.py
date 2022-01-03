# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def hasCycle(self, head: [ListNode]) -> bool:
        slow, fast = head, head

        while fast != None and fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                # print(f"Fast and slow meet here: {slow.val}, {fast.val}")
                return True
        return False

class Solution2:
    def hasCycle(self, head: [ListNode]) -> bool:
        try:
            slow = head
            fast = head.next

            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False
