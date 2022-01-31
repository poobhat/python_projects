"""
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining
elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications
to the input array in place and do not return anything.

Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]


Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 9

"""

class Solution:
    def duplicateZeros(self, arr: [int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        possible_dups = 0
        n = len(arr) - 1

        # Find the number of zeros to be duplicated
        for i in range(n + 1):

            # Stop when i points beyond the last element in the original list
            # which would be part of the modified list
            if i > n - possible_dups:
                break

            # Count the zeros
            if arr[i] == 0:
                # Edge case: This zero can't be duplicated. We have no more space,
                # as i is pointing to the last element which could be included
                if i == n - possible_dups:
                    # arr[n] = 0 # For this zero we just copy it without duplication.
                    n -= 1
                    break
                possible_dups += 1

        # Start backwards from the last element which would be part of new list.
        last = n - possible_dups

        # Copy zero twice, and non zero once.
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                possible_dups -= 1
                arr[i + possible_dups] = 0
            else:
                arr[i + possible_dups] = arr[i]
        print(arr)


s = Solution()
arr = [1,0,1,2,3,4,5,0]
s.duplicateZeros(arr)