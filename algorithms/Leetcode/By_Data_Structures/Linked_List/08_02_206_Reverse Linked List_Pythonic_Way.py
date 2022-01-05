"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        prev = None
        while head:
            prev, prev.next, head = head, prev, head.next
        return prev

    '''
    prev -> null
    head : [1,2,3,4,5]      1 -> 2 -> 3 -> 4 -> 5 -> null
    
    prev = [1]
     null <- 1 
    head : 2,3,4,5
    
    prev : [2]
    null <- 1 <- 2
    head : 3,4,5
    
    prev : [3]
    null <- 1 <- 2 <-3
    head: 4, 5
    
    prev : [4]
   null <- 1 <- 2 <- 3 <- 4
   head: 5
   
   prev: [5]
  null <- 1 <- 2 <- 3 <- 4 <- 5 [5,4,3,2,1]
  head: null
    
    
    
    
    '''