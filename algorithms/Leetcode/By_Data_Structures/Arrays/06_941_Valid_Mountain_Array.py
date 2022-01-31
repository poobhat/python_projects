"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true


Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104

"""
class Solution:
    def validMountainArray(self, arr: [int]) -> bool:
        n = len(arr)-1
        ptr = 0

        while ptr < n and arr[ptr] < arr[ptr+1]:
            ptr += 1

        if ptr == 0 or ptr == n:
            return False

        while ptr < n and arr[ptr] > arr[ptr+1]:
            ptr += 1

        print(ptr, n)
        return ptr == n


s = Solution()
arr = [0,1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1,0]
print(s.validMountainArray(arr))

"""
Time complexity: O(n)
Space complexity: O(1)
"""