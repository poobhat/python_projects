"""
Approach 3: Reverse Second Half In-place

Intuition
The only way we can avoid using O(n) extra space is by modifying the input in-place.

The strategy we can use is to reverse the second half of the Linked List in-place
(modifying the Linked List structure), and then comparing it with the first half.
Afterwards, we should re-reverse the second half and put the list back together.
While you don't need to restore the list to pass the test cases, it is still good
programming practice because the function could be a part of a bigger program that
doesn't want the Linked List broken.

Algorithm

Specifically, the steps we need to do are:

Find the end of the first half.
Reverse the second half.
Determine whether or not there is a palindrome.
Restore the list.
Return the result.

To do step 1, we could count the number of nodes, calculate how many nodes are in the
first half, and then iterate back down the list to find the end of the first half.
Or, we could do it in a single parse using the two runners pointer technique.
Either is acceptable, however we'll have a look at the two runners pointer technique here.

Imagine we have 2 runners one fast and one slow, running down the nodes of the Linked List.
In each second, the fast runner moves down 2 nodes, and the slow runner just 1 node.
By the time the fast runner gets to the end of the list, the slow runner will be half way.
By representing the runners as pointers, and moving them down the list at the corresponding
speeds, we can use this trick to find the middle of the list, and then split the list into
two halves.

If there is an odd-number of nodes, then the "middle" node should remain attached to the
first half.

Step 2 uses the algorithm that can be found in the solution article for the Reverse Linked
List problem to reverse the second half of the list.

Step 3 is fairly straightforward. Remember that we have the first half, which might also
contain a "middle" node at the end, and the second half, which is reversed. We can step
down the lists simultaneously ensuring the node values are equal. When the node we're up
to in the second list is null, we know we're done. If there was a middle value attached
to the end of the first list, it is correctly ignored by the algorithm. The result should
be saved, but not returned, as we still need to restore the list.

Step 4 requires using the same function you used for step 2, and then for step 5 the
saved result should be returned.

"""
"""
Exceeds time limit
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        # Find the end of first half and reverse second half.
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # Check whether or not there's a palindrome.
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # Restore the list and return the result.
        first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous